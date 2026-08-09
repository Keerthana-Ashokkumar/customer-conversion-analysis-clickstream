## Tesla Stock Price Prediction Using SimpleRNN and LSTM
## Project Overview

This project focuses on predicting Tesla's future closing stock prices using deep learning models. The solution compares SimpleRNN and LSTM models for 1-day, 5-day and 10-day ahead forecasting, evaluates their performance using MSE, RMSE and MAE, and performs LSTM hyperparameter tuning using GridSearchCV.

## Domain

Financial Analytics | Data Science | Deep Learning | Time-Series Forecasting

## Problem Statement

Tesla stock prices are highly dynamic and can be affected by market trends, volatility and external events. The objective is to develop a time-series forecasting system that can predict future Tesla closing prices and compare the performance of SimpleRNN and LSTM architectures.

## Business Use Cases
Short-Term Stock Price Forecasting
Investment Decision Support
Risk & Volatility Assessment
Portfolio Planning
Market Trend Analysis
Financial Analyst Decision Support
News-Sentiment-Based Market Analysis

## Dataset Description

Dataset: Tesla historical stock-price data (TSLA.csv)

Records: 2,416
Period: June 2010 – February 2020
Features: Date, Open, High, Low, Close, Adj Close, Volume.

## Approach

1️⃣ Data Preprocessing

Missing-value checking
Duplicate checking
Date conversion and sorting
Time-series train/test split
MinMax scaling
Training-only scaler fitting to avoid data leakage.

2️⃣ Exploratory Data Analysis

Closing-price trend
Trading volume
Moving averages
Daily returns / volatility
Feature distributions
Correlation analysis
Outlier analysis.

3️⃣ Feature Engineering
Main prediction feature:

Adjusted Closing Price

A 60-day historical window is used to predict:

1-day ahead
5-day ahead
10-day ahead.

4️⃣ Modeling Techniques

🔹 Deep Learning – Time Series

SimpleRNN
LSTM

🔹 Hyperparameter Optimization

GridSearchCV
Units
Dropout
Learning Rate

🔹 NLP Extension

VADER sentiment analysis on Tesla news headlines.
5️⃣ Model Evaluation

Evaluation Metrics

MSE
RMSE
MAE

Lower RMSE/MAE indicates better prediction performance.

6️⃣ Forecasting

The project performs:

1-day prediction
5-day prediction
10-day prediction
10-day recursive forward forecasting using the LSTM 1-day model.
7️⃣ Model Comparison

Based on the actual .md evaluation output:

Horizon	Better Model
1-Day	LSTM
5-Day	SimpleRNN
10-Day	SimpleRNN

The corresponding RMSE values in the file are approximately:

Horizon	LSTM	SimpleRNN
1-Day	26.45	27.08
5-Day	42.28	40.67
10-Day	51.10	46.87

8️⃣ Hyperparameter Tuning

GridSearchCV tested:

Units: 32, 64
Dropout: 0.2, 0.3
Learning rate: 0.001, 0.005

The best CV configuration recorded in the file is:

64 units + 0.3 dropout + 0.005 learning rate.

9️⃣ NLP — News Sentiment

Tesla-related headlines are cleaned and analysed using VADER sentiment analysis. Sentiment scores are then compared with same-day Tesla returns.

This provides a pathway to add news sentiment as an additional model input, rather than relying only on historical prices.

🌐 Application / Business Output

Your Tesla project can be presented as a Financial Decision Support System:

Input → Historical Tesla Data + News Sentiment

Processing → Preprocessing → 60-Day Sequence → Deep Learning Model

Output →

Predicted stock price
Forecast horizon
Model performance
Risk/trend information
Optional sentiment signal

## 📈 Skills Learned
Data Cleaning & Preprocessing
Time-Series EDA
Feature Engineering
Deep Learning
SimpleRNN
LSTM
Model Evaluation
Hyperparameter Tuning
Recursive Forecasting
NLP / Sentiment Analysis
End-to-End ML Pipeline
🧰 Technology Stack
Category	Tools
Programming	Python
Data Handling	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Machine Learning	Scikit-learn
Deep Learning	TensorFlow / Keras
NLP	VADER
Model Tuning	GridSearchCV / SciKeras
Model Saving	Keras model files

The actual notebook uses TensorFlow/Keras, Scikit-learn, Pandas, NumPy, Matplotlib and Seaborn.
