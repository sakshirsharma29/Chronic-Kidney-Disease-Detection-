# Chronic Kidney Disease Detection using Machine Learning

## Overview

This project focuses on the early detection of Chronic Kidney Disease (CKD) using supervised machine learning algorithms. The goal is to assist in timely diagnosis by identifying patterns in patient medical data, thereby enabling preventive healthcare decisions.

The model is trained on medical records from the CKD dataset and predicts whether a patient is likely to have CKD based on clinical features. It offers a lightweight interface to input data and receive instant predictions.

---

## Features

- Predicts the presence of CKD based on patient medical data
- Uses machine learning algorithms for classification
- Built-in data cleaning and preprocessing pipeline
- Easy-to-use web interface for real-time prediction
- Trained and evaluated on real-world dataset from UCI repository

---

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib / Seaborn (for visualization)
- Flask (for web deployment)
- HTML/CSS (frontend)

---

## Dataset

(Already Provided from kaggle): [kidney_disease.csv…]()


Preprocessing steps included:
- Handling missing values
- Label encoding of categorical variables
- Feature scaling


---

## Model Training

Multiple machine learning models were trained and evaluated, including:

- Logistic Regression
- Random Forest Classifier
- ANN
- Decision Tree

The final model was selected based on performance metrics and generalization ability.

---

## Performance Metrics

| Model              | Accuracy | Precision | Recall | F1 Score |
|-------------------|----------|-----------|--------|----------|
| Random Forest      | 98.5%    | 98.7%     | 98.3%  | 98.5%    |
| Logistic Regression| 96.0%    | 95.8%     | 96.2%  | 96.0%    |

These metrics were calculated on the test set using 80-20 train-test split.

---

Webpage UI:

<img width="887" height="434" alt="UI(CKD)" src="https://github.com/user-attachments/assets/926d8e75-9653-4fe4-abde-d64f65bbe8b8" />


