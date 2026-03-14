#  Customer Conversion Analysis for Online Shopping Using Clickstream Data

## 📌 Project Overview

This project focuses on analyzing e-commerce clickstream data to **predict customer conversion**, **estimate potential revenue**, and **segment customers** based on their browsing behavior.
The solution integrates **data preprocessing, feature engineering, machine learning model building, evaluation, and deployment** through an interactive **Streamlit web application**.

The system helps businesses understand customer behavior, improve marketing strategies, and increase overall conversion rates using data-driven insights.


## 🏫 Domain

**E-commerce Analytics / Data Science / Machine Learning**


## ❓ Problem Statement

E-commerce platforms generate massive volumes of clickstream data that capture customer browsing behavior. However, converting this raw data into actionable insights is challenging.

The goal of this project is to build an intelligent system that can:

* Predict whether a customer will complete a purchase
* Estimate the revenue a customer is likely to generate
* Segment customers into meaningful groups for targeted marketing

This enables businesses to optimize user experience, improve conversions, and maximize revenue.

---

## 💼 Business Use Cases

* **Customer Conversion Prediction** – Identify users likely to make a purchase
* **Revenue Forecasting** – Predict potential customer spending
* **Customer Segmentation** – Group users based on browsing behavior
* **Targeted Marketing** – Enable personalized campaigns
* **Churn Reduction** – Identify users likely to abandon sessions
* **Product Recommendation Optimization**

---

## 📊 Dataset Description

**Dataset Source:** UCI Machine Learning Repository – Clickstream Data

### Key Features

| Column Name       | Description                           |
| ----------------- | ------------------------------------- |
| Year              | Year of session                       |
| Month             | Month of session                      |
| Day               | Day of the month                      |
| Order             | Click sequence within a session       |
| Country           | Country code of user                  |
| Session ID        | Unique session identifier             |
| Main Category     | Primary product category              |
| Clothing Model    | Product identifier                    |
| Colour            | Product color                         |
| Location          | Image location on page                |
| Model Photography | Photography type                      |
| Price             | Product price (USD)                   |
| Price 2           | Price above category average (Yes/No) |
| Page              | Page number visited                   |

---

## 🔍 Approach

### 1️⃣ Data Preprocessing

* Handling missing values
* Removing irrelevant and high-cardinality features
* Encoding categorical variables
* Feature scaling using **StandardScaler**

### 2️⃣ Exploratory Data Analysis (EDA)

* Univariate and bivariate analysis
* Correlation analysis
* Session-level behavior analysis
* Outlier detection

### 3️⃣ Feature Engineering

* Session-based metrics (total clicks, average price)
* Behavioral indicators (high price views, weekend visits)
* Aggregated session features

### 4️⃣ Modeling Techniques

#### 🔹 Classification

* Logistic Regression
* Decision Tree
* **Random Forest (Final Model)**
  (Target: Customer Conversion)

#### 🔹 Regression

* Linear Regression
* **Gradient Boosting Regressor (Final Model)**
  (Target: Revenue Estimation)

#### 🔹 Clustering

* **K-Means Clustering**
  (Customer Segmentation)

### 5️⃣ Model Evaluation

* **Classification:** Accuracy, Precision, Recall, F1-score, ROC-AUC
* **Regression:** MAE, RMSE, R² Score
* **Clustering:** Silhouette Score, Davies–Bouldin Index

### 6️⃣ Model Saving & Pipelines

* Trained models saved using `joblib`
* Reusable ML pipeline structure

---

## 🌐 Streamlit Application

### 🔹 Features

* User-friendly sidebar input for clickstream details
* Real-time prediction of:

  * Customer conversion (Yes/No)
  * Estimated revenue
  * Customer segment (cluster)
* Interactive and business-ready dashboard

### 🔹 Tech

* Built using **Streamlit**
* Integrated trained ML models
* Supports real-time inference

---

## 📈 Skills Learned

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Supervised & Unsupervised Machine Learning
* Model Evaluation & Hyperparameter Tuning
* End-to-End ML Pipeline Development
* Streamlit Web Application Development
* Model Deployment

---

## 🧰 Technology Stack

| Category             | Tools                                                  |
| -------------------- | ------------------------------------------------------ |
| Programming Language | Python                                                 |
| Data Handling        | Pandas, NumPy                                          |
| Visualization        | Matplotlib, Seaborn                                    |
| Machine Learning     | Scikit-learn                                           |
| Model Serialization  | Joblib                                                 |
| Web Application      | Streamlit                                              |
| Concepts             | Classification, Regression, Clustering, EDA, Pipelines |

---

## 📦 Project Deliverables

* Data preprocessing & feature engineering notebooks
* Machine learning model scripts
* Trained model files (`.pkl`)
* Streamlit application (`app.py`)
* Model evaluation results
* `requirements.txt`
* Project documentation (`README.md`)

---
