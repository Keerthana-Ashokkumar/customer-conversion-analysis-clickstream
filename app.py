import streamlit as st
import pandas as pd
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Customer Conversion Analysis",
    layout="wide"
)

st.title("Customer Conversion Analysis for Online Shopping")
st.write("Predict Conversion, Revenue & Customer Segment using Clickstream Data")

# --------------------------------------------------
# Load Trained Models
# --------------------------------------------------
clf_model = joblib.load("models/classification_model.pkl")
reg_model = joblib.load("models/regression_model.pkl")
cluster_model = joblib.load("models/clustering_model.pkl")

# --------------------------------------------------
# Load Feature Template (CRITICAL)
# --------------------------------------------------
X_template = pd.read_csv("data/X_classification.csv")

# VERY IMPORTANT: column names must be STRING
X_template.columns = X_template.columns.astype(str)

# --------------------------------------------------
# Sidebar Inputs (USER FRIENDLY UI)
# --------------------------------------------------
st.sidebar.header("Input Customer Clickstream Details")

year = st.sidebar.slider("Year", 2010, 2025, 2012)
month = st.sidebar.slider("Month", 1, 12, 6)
day = st.sidebar.selectbox(
    "Day",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

day_map = {
    "Monday": 1, "Tuesday": 2, "Wednesday": 3,
    "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7
}

country = st.sidebar.selectbox(
    "Country",
    ["India", "USA", "UK", "Germany", "France", "Other"]
)

country_map = {
    "India": 91,
    "USA": 1,
    "UK": 44,
    "Germany": 49,
    "France": 33,
    "Other": 0
}

click_order = st.sidebar.slider("Click Order", 1, 20, 1)
session_id = st.sidebar.slider("Session ID (normalized)", 0.0, 1.0, 0.05)
price = st.sidebar.slider("Product Price ($)", 10, 1000, 200)
page_no = st.sidebar.slider("Page Number", 1, 50, 1)

# --------------------------------------------------
# Build Input Data (MODEL SAFE)
# --------------------------------------------------
input_data = X_template.mean().to_dict()

input_data["0"] = year
input_data["1"] = month
input_data["2"] = day_map[day]
input_data["3"] = click_order
input_data["4"] = country_map[country]
input_data["5"] = session_id
input_data["11"] = price
input_data["13"] = page_no

input_df = pd.DataFrame([input_data])
input_df.columns = input_df.columns.astype(str)

# --------------------------------------------------
# Prediction Button
# --------------------------------------------------
if st.button("Predict"):

    # ---- Classification ----
    conv_pred = clf_model.predict(input_df)[0]
    conv_prob = clf_model.predict_proba(input_df)[0][1]

    # ---- Regression ----
    revenue_pred = reg_model.predict(input_df)[0]

    # ---- Clustering ----
    cluster_pred = cluster_model.predict(input_df)[0]

    # --------------------------------------------------
    # Results
    # --------------------------------------------------
    st.subheader("Prediction Results")

    if conv_pred == 1:
        st.success(f"✅ Customer WILL Convert (Probability: {conv_prob:.2f})")
    else:
        st.error(f"❌ Customer will NOT Convert (Probability: {conv_prob:.2f})")

    st.info(f"💰 Estimated Revenue: ${revenue_pred:.2f}")
    st.warning(f"👥 Customer Segment: Cluster {cluster_pred}")
