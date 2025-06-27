
#  One-Shot Facial Recognition with Siamese Networks

This repository implements a robust **one-shot face recognition system** using **Siamese Neural Networks (SNNs)**. Designed to recognize individuals from a single reference image, it enables efficient verification even with limited data. The project also includes a **Kivy-based GUI app** for real-time face recognition and user interaction.

>  One-shot learning — No retraining needed  
>  Works with few samples per identity  
>  Robust to noise, brightness, and orientation changes  
>  Includes a desktop GUI via Kivy

---

##  Project Overview

Traditional facial recognition systems require large labeled datasets and retraining. This project avoids that by training a Siamese Neural Network to **compare pairs of faces** and determine their similarity using a learned embedding space.

The system includes:
- Face detection and preprocessing
- Twin CNNs with shared weights (`layers.py`)
- Similarity scoring based on L1 distance
- Real-time classification via GUI (`faceid.py`)
- Manual dataset preparation via folders (`anchor/`, `positive/`, `negative/`)

---

## 📁 Project Structure

```bash
.
├── siamese_network.ipynb     # Notebook for training, testing, and demos
├── layers.py                 # Siamese CNN architecture (imported in Kivy app)
├── faceid.py                 # Kivy GUI app for real-time face verification
├── anchor/                   # (Create) Reference identity images
├── positive/                 # (Create) Matching identity images
├── negative/                 # (Create) Different identity images
├── README.md                 # Project documentation

````

>  You must create and populate `anchor/`, `positive/`, and `negative/` directories with face images before training or testing.

---

##  Kivy App: Real-Time Face Verification

A major feature of this project is the **graphical user interface built using Kivy**, designed for user-friendly interaction and real-time identity verification.

###  Files:

* **`faceid.py`**: Main Kivy app file; captures user input and matches faces against anchor images.
* **`layers.py`**: Contains the CNN architecture used for embedding generation.

###  Features:

* Webcam-based real-time face capture
* Visual similarity score output (0 to 1)
* Displays match results instantly
* Portable and minimal — works on any desktop OS with Python

> You can extend the app for use cases like access control, attendance marking, or desktop login.

---

##  Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/one-shot-face-recognition.git
cd one-shot-face-recognition
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Prepare Data

* Create folders: `anchor/`, `positive/`, `negative/`
* Add face images accordingly:

  * `anchor/`: Reference face (one per identity)
  * `positive/`: Same person as anchor
  * `negative/`: Different individuals

### 4. Run the Notebook (optional)

```bash
jupyter notebook siamese_network.ipynb
```

### 5. Run the Kivy App

```bash
python faceid.py
```

---

##  Performance (Evaluated)

| **Metric**                   | **Result** |
| ---------------------------- | ---------- |
| One-shot accuracy (Omniglot) | 92.0%      |
| Verification accuracy        | 93.4%      |
| Adversarial ε = 0.1          | \~77.4%    |
| OOD rejection rate           | \~86%      |

---

##  Highlights

*  **Siamese Architecture**: Learns to compare faces, not memorize identities.
*  **Visual GUI**: Lightweight desktop app for face matching.
*  **Augmentation-Ready**: Rotation, noise, contrast handled in preprocessing.
*  **Real-Time Demo**: Interactively match faces with webcam or image upload.

---

##  References

* Koch et al. (2015) – *Siamese Neural Networks for One-shot Image Recognition*
* Abbas et al. (2023) – *ConvMixer + AdaBoost for Masked Face Recognition*
* Zhang & Chi (2020) – *End-to-End Face Detection and Recognition*
* Haq et al. (2025) – *Review of Face Detection and Recognition Algorithms*

