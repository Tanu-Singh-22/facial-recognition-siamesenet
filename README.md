
# One-Shot Facial Recognition with Siamese Networks

This project implements a robust **one-shot face recognition system** using **Siamese Neural Networks (SNNs)**. It is designed to recognize individuals from a single reference image, making it ideal for use cases where large labeled datasets are not available or retraining is impractical.

>  Learns to compare, not classify  
>  Generalizes to unseen identities  
>  Robust to adversarial noise, lighting changes, and image rotation  
>  Useful for authentication, access control, and surveillance applications

---

## Overview

Traditional facial recognition systems rely on labeled datasets and fixed class labels. In contrast, Siamese Networks learn a **similarity function** between image pairs, enabling powerful one-shot learning and identity verification. This repository provides an end-to-end pipeline:

- Face detection and preprocessing
- Twin CNNs for feature embedding
- L1-based similarity scoring
- One-shot classification logic
- Adversarial and OOD robustness testing

---

## Project Structure

```
.
├── siamese_network.ipynb     # Jupyter notebook with model, training, and evaluation
├── anchor/                   # (Create) Reference identity images
├── positive/                 # (Create) Images of same identity as anchor
├── negative/                 # (Create) Images of different identities
├── README.md                 # Project documentation
````

> ⚠️ **Note**: The `anchor/`, `positive/`, and `negative/` folders need to be manually created and populated by you.
> These are essential for training and testing the model.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/one-shot-face-recognition.git
cd one-shot-face-recognition
```

### 2. Prepare Data

* Create three folders: `anchor/`, `positive/`, and `negative/`
* Add face images in each, following the structure:

  * `anchor/` → Reference faces (1 per identity)
  * `positive/` → Same person as in anchor
  * `negative/` → Different individuals

### 3. Launch the Notebook

```bash
jupyter notebook siamese_network.ipynb
```

---

## 📊 Evaluation

| **Metric**                   | **Result** |
| ---------------------------- | ---------- |
| One-shot accuracy (Omniglot) | 92.0%      |
| Verification accuracy        | 93.4%      |
| Adversarial ε = 0.1          | \~77.4%    |
| OOD rejection rate           | \~86%      |

---

## 💡 Features

* 📎 **Siamese Architecture**: Twin CNNs with shared weights for embedding generation.
* 📏 **L1 Distance Scoring**: Custom `L1Dist` layer computes similarity between embeddings.
* 🔐 **Adversarial Robustness**: Tested under noise and perturbation attacks.
* 🌩️ **Environmental Variance**: Handles rotation, contrast, and lighting changes.
* 🧠 **One-Shot Learning**: Works with just one sample per class—no retraining required.

---

## 🛠 Built With

* Python 3.10
* TensorFlow & Keras
* OpenCV (face detection)
* NumPy, Matplotlib
* Jupyter Notebook

---

## 📚 References

* Koch et al. (2015). *Siamese Neural Networks for One-shot Image Recognition*.
* Abbas et al. (2023). *ConvMixer + AdaBoost for Masked Face Recognition*.
* Zhang & Chi (2020). *End-to-End Face Detection and Recognition*.
* Haq et al. (2025). *Review of Face Detection and Recognition Algorithms*.

---
