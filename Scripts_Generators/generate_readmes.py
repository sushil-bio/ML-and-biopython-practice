import os

readme_tp53 = """# 🔬 TP53 Gene Expression Analysis

## Overview
This repository contains a computational biology pipeline that analyzes **gene expression data** to identify **driving mutations** in cancer tissue. By using Machine Learning, we can discover which specific genes are most critical for diagnosing malignant tumors.

## Features
- **Data Processing:** Loaded and cleaned a dataset containing 50 gene columns using **Pandas**.
- **Machine Learning Inference:** Trained a **RandomForestClassifier** to diagnose patients based entirely on their gene expression levels with extremely high accuracy.
- **Feature Importance Mapping:** Extracted the internal logic of the Random Forest and plotted a bar chart using **Matplotlib** to visually prove that the mutation of the TP53 gene is the primary driver of the cancer diagnosis.

## Tech Stack
- **Language:** Python
- **Data Engineering:** Pandas
- **Machine Learning:** Scikit-Learn
- **Visualization:** Matplotlib"""

readme_cnn = """# 🩸 Blood Cell Diagnosis CNN

## Overview
This deep learning medical image classifier is built using the **MedMNIST** dataset. It features a Convolutional Neural Network (CNN) architecture trained to visually diagnose 8 different types of microscopic blood cell images with near 90% accuracy.

## Features
- **Computer Vision Extraction:** Built sequential `Conv2D` and `MaxPooling2D` feature extraction layers to act as the "eyes" of the model.
- **Deep Learning Diagnosis:** Flattened multi-dimensional pixel matrices into a `Dense` neural network core to diagnose cell types.
- **Scientific Visualization:** Used Matplotlib and NumPy arrays to map AI visual predictions against true medical pathology labels.

## Tech Stack
- **Language:** Python
- **Deep Learning:** TensorFlow / Keras
- **Computer Vision Framework:** MedMNIST, Matplotlib, NumPy"""

# The destination folders
base_dir = r"C:\Users\mules\Documents"
tp53_dir = os.path.join(base_dir, "TP53-Gene-Expression")
cnn_dir = os.path.join(base_dir, "Blood-Cell-CNN")

# Only generate them if the folders actually exist 
if os.path.exists(tp53_dir) and os.path.exists(cnn_dir):
    with open(os.path.join(tp53_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_tp53)
        print("✅ TP53 README.md created!")

    with open(os.path.join(cnn_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_cnn)
        print("✅ Blood-Cell-CNN README.md created!")
else:
    print("Oops! I couldn't find the folders in C:\\Users\\mules\\Documents")
