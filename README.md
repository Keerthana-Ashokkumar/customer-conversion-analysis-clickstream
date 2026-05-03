## Customer Conversion Analysis for Online Shopping Using Clickstream Data

## Project Overview
This project focuses on analyzing e-commerce clickstream data to predict customer conversion, estimate potential revenue, and perform customer segmentation based on browsing behavior.
The solution covers the complete machine learning pipeline, including:
•	Data preprocessing 
•	Exploratory Data Analysis (EDA) 
•	Feature engineering 
•	Model building and evaluation 
•	Deployment using a Streamlit web application 

## Domain
## E-commerce Analytics | Data Science | Machine Learning

## Problem Statement
E-commerce platforms generate massive volumes of clickstream data that capture user browsing behavior. However, extracting meaningful insights from this data is challenging.
The goal of this project is to build an intelligent system that can:
•	Predict whether a customer will complete a purchase 
•	Estimate the revenue a customer is likely to generate 
•	Segment customers into meaningful groups 

## Business Use Cases
•	Customer Conversion Prediction 
•	Revenue Forecasting 
•	Customer Segmentation 
•	Targeted Marketing Campaigns 
•	Churn Reduction 
•	Product Recommendation Optimization 

## Dataset Description
## Dataset Source: UCI Machine Learning Repository – Clickstream Data
## Key Features
Column Name	Description
Year	Year of session
Month	Month of session
Day	Day of the month
Order	Click sequence
Country	User country
Session ID	Unique session identifier
Main Category	Product category
Clothing Model	Product ID
Colour	Product color
Location	Page image location
Model Photography	Photography type
Price	Product price (USD)
Price 2	Price above category average
Page	Page number visited

##  Approach
## 1️⃣ Data Preprocessing
•	Handling missing values 
•	Removing irrelevant/high-cardinality features 
•	Encoding categorical variables 
•	Feature scaling using StandardScaler 

## 2️⃣ Exploratory Data Analysis (EDA)
•	Univariate analysis (distribution) 
•	Bivariate analysis (relationships) 
•	Correlation heatmap 
•	Session behavior analysis 
•	Outlier detection 

## 3️⃣ Feature Engineering
Created meaningful features to capture user behavior:
•	Session Features 
o	total_clicks 
o	avg_price 
o	max_page 
o	unique_products 
•	Behavioral Features 
o	high_price_view 
o	is_weekend 

## 4️⃣ Modeling Techniques
## 🔹 Classification (Customer Conversion)
•	Logistic Regression 
•	Decision Tree 
•	Random Forest ✅ (Final Model) 

## 🔹 Regression (Revenue Prediction)
•	Linear Regression 
•	Gradient Boosting Regressor ✅ (Final Model) 

## 🔹 Clustering (Customer Segmentation)
•	K-Means Clustering ✅ (Final Model) 

## 5️⃣ Model Evaluation
## Classification Metrics
•	Accuracy 
•	Precision 
•	Recall 
•	F1-score 
•	ROC-AUC 
## Regression Metrics
•	MAE 
•	RMSE 
•	R² Score 
## Clustering Metrics
•	Silhouette Score 
•	Davies–Bouldin Index 

## 6️⃣ Model Saving & Pipelines
•	Models saved using joblib 
•	Reusable ML workflow created 
•	Supports deployment and inference 

## 🌐 Streamlit Application
🔹 Features
•	User-friendly input interface 
•	Real-time predictions 
🔹 Outputs
•	Customer Conversion (Yes / No) 
•	Estimated Revenue 
•	Customer Segment (Cluster) 
🔹 Tech Stack
•	Built using Streamlit 
•	Integrated trained ML models 
•	Supports real-time predictions 

## 📈 Skills Learned
•	Data Cleaning & Preprocessing 
•	Exploratory Data Analysis (EDA) 
•	Feature Engineering 
•	Machine Learning (Supervised & Unsupervised) 
•	Model Evaluation & Tuning 
•	End-to-End ML Pipeline Development 
•	Streamlit Web App Development 
•	Model Deployment 

## 🧰 Technology Stack
Category	Tools
Programming	Python
Data Handling	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Machine Learning	Scikit-learn
Model Saving	Joblib
Web App	Streamlit

## 📦 Project Deliverables
•	Data preprocessing & feature engineering notebooks 
•	Model training scripts 
•	Trained model files (.pkl) 
•	Streamlit application (app.py) 
•	Model evaluation results 
•	requirements.txt 
•	Project documentation (README.md) 
.

