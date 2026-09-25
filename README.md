# Data Classification Using AI

## DecodeLabs – Artificial Intelligence Project 2

### 📌 Project Overview

This project is part of the **DecodeLabs Artificial Intelligence Industrial Training – Project 2**.

The objective is to build a basic **data classification model using supervised learning**. The project demonstrates how a dataset can be prepared, divided into training and testing data, used to train a classification model, and evaluated on unseen data.

The project follows the key requirements provided by DecodeLabs: understanding a dataset, splitting it into training and testing sets, and applying a simple classification algorithm.

---

## 🎯 Objectives

* Load and understand a dataset
* Prepare the data for classification
* Split the dataset into training and testing sets
* Implement a classification algorithm
* Train the classification model
* Test the model using unseen data
* Calculate classification performance metrics
* Predict classes for new data

---

## 🧠 Concepts Used

* Artificial Intelligence
* Supervised Learning
* Data Classification
* Training and Testing Data
* Feature Scaling
* K-Nearest Neighbors (KNN)
* Euclidean Distance
* Accuracy
* Confusion Matrix
* Precision
* Recall
* F1-Score

---

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Matplotlib**

The classification algorithm is implemented directly in Python rather than relying on a machine-learning library for the KNN logic.

---

## 📂 Project Structure

```text
DecodeLabs_Project2-Data-Classification-Using-AI/
│
├── dataclassificationwithai.py
└── README.md
```

---

## ⚙️ How It Works

The project follows these main steps:

### 1. Dataset Preparation

A small classification dataset is prepared with multiple numerical features and corresponding class labels.

### 2. Train-Test Split

The dataset is divided into:

* **Training data** – used to build the model
* **Testing data** – used to evaluate the model

### 3. Feature Scaling

The numerical features are standardized using the mean and standard deviation calculated from the training data.

### 4. KNN Classification

The **K-Nearest Neighbors (KNN)** algorithm is implemented using Euclidean distance.

For a new data point:

1. Calculate its distance from the training samples.
2. Select the nearest `K` samples.
3. Find the majority class among those samples.
4. Assign that class to the new data point.

### 5. Model Evaluation

The model is evaluated using:

* Accuracy
* Confusion Matrix
* Precision
* Recall
* F1-Score

### 6. New Predictions

The trained classification model is also used to classify new, previously unseen samples.

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/nagajagannadhsingh/DecodeLabs_Project2-Data-Classification-Using-AI-.git
```

### Step 2: Open the Project

```bash
cd DecodeLabs_Project2-Data-Classification-Using-AI-
```

### Step 3: Run the Program

```bash
python dataclassificationwithai.py
```

---

## 📊 Expected Output

The program displays:

```text
Dataset information
Training and testing data
KNN classification results
Accuracy
Confusion Matrix
Precision
Recall
F1-Score
Predictions for new samples
```

A confusion matrix visualization is also generated using Matplotlib.

---

## 📚 Learning Outcomes

Through this project, the following skills are demonstrated:

* Basic data handling
* Understanding supervised learning
* Training and testing a classification model
* Understanding the KNN algorithm
* Calculating model evaluation metrics
* Making predictions on new data

These align with the key skills listed for DecodeLabs Project 2.

---

## 👨‍💻 Author

**Naga Jagannadh Singh**

B.Tech – Computer Science and Engineering
2nd Year Student

### Internship

**DecodeLabs – Artificial Intelligence Industrial Training**

---

## 🔗 GitHub Repository

[DecodeLabs Project 2 – Data Classification Using AI](https://github.com/nagajagannadhsingh/DecodeLabs_Project2-Data-Classification-Using-AI-)

---

## 📜 Project

**DecodeLabs Artificial Intelligence – Project 2**

**Project Title:** Data Classification Using AI
