from kivy.app import App
from kivy.uix.boxlayout import BoxLayout



from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.logger import Logger

import cv2
import tensorflow as tf
from layers import L1Dist
import os
import numpy as np

class CamApp(App):
    def build(self):
        self.web_cam = Image(size_hint=(1,.8))
        self.button = Button(text="Verify",on_press = self.verify, size_hint=(1,.1))
        self.verification_label= Label(text="Verification Uninitiated", size_hint=(1,.1))

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.web_cam)
        layout.add_widget(self.button)
        layout.add_widget(self.verification_label)

        # load keras model
        self.model = tf.keras.models.load_model('siamesemodel.keras',custom_objects={'L1Dist':L1Dist})

        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update,1.0/33.0)

        return layout

    def update(self,*args):
        # read from opencv
        ret,frame = self.capture.read()
        frame = frame[120:120+250,200:200+250,:]

        #flip horizontal and convert image to texture
        buf = cv2.flip(frame,0).tostring()
        img_texture = Texture.create(size = (frame.shape[1],frame.shape[0]),colorfmt = 'bgr')
        img_texture.blit_buffer(buf,colorfmt='bgr',bufferfmt='ubyte')
        self.web_cam.texture = img_texture

    def preprocess(self,file_path):
        # read image from file path into raw byte format.
        byte_img = tf.io.read_file(file_path)
        # Decodes the JPEG image into a TensorFlow tensor
        img = tf.io.decode_jpeg(byte_img)
        #preprocessing steps  = resizing the image ot be 100x100x3 
        img = tf.image.resize(img,(100,100))
        img = img / 255.0
        # Normalizes pixel values from [0, 255] to [0.0, 1.0].
        return img

    def verify(self,*args):
        detection_threshold = 0.5
        verification_threshold = 0.8

        # capture input image from webcam
        SAVE_PATH = os.path.join('application_data', 'input_image', 'input_image.jpg')
        ret,frame = self.capture.read()
        frame = frame[120:120+250,200:200+250,:]
        cv2.imwrite(SAVE_PATH,frame)

        # Build results array
        results = []
        for image in os.listdir(os.path.join('application_data', 'verification_images')):
            input_img = self.preprocess(os.path.join('application_data', 'input_image', 'input_image.jpg'))
            validation_img = self.preprocess(os.path.join('application_data', 'verification_images', image))
            
            # Make Predictions 
            result = self. model.predict(list(np.expand_dims([input_img, validation_img], axis=1)))
            results.append(result)
        
        # Detection Threshold: Metric above which a prediciton is considered positive 
        detection = np.sum(np.array(results) > detection_threshold)
        
        # Verification Threshold: Proportion of positive predictions / total positive samples 
        verification = detection / len(os.listdir(os.path.join('application_data', 'verification_images'))) 
        verified = verification > verification_threshold

        self.verification_label.text = 'Verified' if verified ==True else'Unverified' 

        Logger.info(results)
        Logger.info(detection)
        Logger.info(verification)
        Logger.info(verified)
        
        return results, verified


if __name__ == '__main__':
    CamApp().run()

