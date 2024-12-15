# Cataract detection using ML 
  1. Used OpenCV, Keras, image processing and python concepts. 
  2. Created a software that helps to detect the Cataract disease from the fundus images

#### • Cataract

<img src="img/Cataract/01.jpg.png" width="128"/> <img src="img/Cataract/02.jpg.png" width="128"/>

#### • Normal

<img src="img/Normal/01_h.jpg" width="128"/> <img src="img/Normal/02_h.jpg" width="128"/>

# CNN-based Image Classification Project

## Overview
This project implements a Convolutional Neural Network (CNN) using TensorFlow and Keras to classify image data. The dataset is preprocessed and saved as pickle files (`X.pickle` and `y.pickle`), which are loaded and used to train the model.

## Features
1. **Data Preprocessing**:
   - Normalizes input images to scale pixel values between 0 and 1.
   - Supports loading data from pickle files.

2. **Model Architecture**:
   - Uses a sequential model with Conv2D, MaxPooling2D, and Dense layers.
   - Includes activation functions such as ReLU and Sigmoid for better performance.

3. **Training and Validation**:
   - Splits the dataset for training and validation.
   - Compiles the model with Adam optimizer and binary cross-entropy loss.

## Requirements
To run this project, ensure you have the following installed:

### Libraries:
- TensorFlow
- Keras
- Pickle

Install these dependencies with:
```bash
pip install tensorflow
```

### Dataset:
- Preprocessed dataset saved as `X.pickle` and `y.pickle`.

## How to Run
1. Clone or download this repository to your local system.

2. Ensure the pickle files (`X.pickle` and `y.pickle`) are in the same directory as the script.

3. Run the training script with:
```bash
python your_script_name.py
```

4. The model will train for 1 epoch (default setting) and print training/validation accuracy and loss.

## Model Architecture
1. **Input Layer**:
   - Accepts images with shape based on the preprocessed data (`X.shape[1:]`).

2. **Convolutional Layers**:
   - Extracts spatial features using Conv2D layers with 256 filters and a 3x3 kernel.

3. **Pooling Layers**:
   - Reduces spatial dimensions using MaxPooling2D with a 2x2 pool size.

4. **Fully Connected Layers**:
   - Flattens the feature maps and connects to Dense layers.
   - Final Dense layer with a Sigmoid activation for binary classification.

## Training Details
- **Optimizer**: Adam
- **Loss Function**: Binary Crossentropy
- **Metrics**: Accuracy
- **Batch Size**: 32
- **Epochs**: 1 (default)
- **Validation Split**: 30%

## Example Output
During training, you will see outputs similar to:
```text
Epoch 1/1
- loss: 0.6931 - accuracy: 0.5000 - val_loss: 0.6928 - val_accuracy: 0.5123
```

## Authors
- **Satyam Gupta** 

## Acknowledgments
- TensorFlow and Keras for providing robust libraries for deep learning.

## Disclaimer
This project is for educational purposes and not intended for commercial use or real-world deployment.


