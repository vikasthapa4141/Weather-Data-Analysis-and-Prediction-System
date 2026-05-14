# ============================================
# WEATHER DATA ANALYSIS AND PREDICTION APP
# STREAMLIT GUI APPLICATION
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import pickle
import warnings
warnings.filterwarnings('ignore')

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Weather Prediction System",
    page_icon="🌦️",
    layout="wide"
)

# ============================================
# TITLE
# ============================================

st.title("🌦️ Weather Data Analysis and Prediction")
st.markdown("---")

# ============================================
# SIDEBAR
# ============================================

st.sidebar.header("📂 Upload Weather Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# ============================================
# LOAD DATA
# ============================================

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Uploaded Successfully!")

    # ============================================
    # SHOW DATASET
    # ============================================

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    # ============================================
    # DATA PREPROCESSING
    # ============================================

    st.subheader("🛠️ Data Preprocessing")

    st.write("Missing Values:")
    st.write(df.isnull().sum())

    # Remove missing values
    df.dropna(inplace=True)

    # Convert Date column
    df['Date'] = pd.to_datetime(df['Date'])

    # Create Date Features
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day

    st.success("Data Preprocessing Completed!")

    # ============================================
    # DATA VISUALIZATION
    # ============================================

    st.subheader("📈 Temperature Trend")

    fig1, ax1 = plt.subplots(figsize=(12, 5))

    ax1.plot(df['Date'], df['Temperature'])

    ax1.set_title("Temperature Trend Over Time")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Temperature")

    st.pyplot(fig1)

    # ============================================
    # MONTHLY AVERAGE TEMPERATURE
    # ============================================

    st.subheader("📊 Monthly Average Temperature")

    monthly_avg = df.groupby('Month')['Temperature'].mean()

    fig2, ax2 = plt.subplots(figsize=(10, 5))

    monthly_avg.plot(kind='bar', ax=ax2)

    ax2.set_title("Monthly Average Temperature")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Average Temperature")

    st.pyplot(fig2)

    # ============================================
    # FEATURE SELECTION
    # ============================================

    X = df[['Year', 'Month', 'Day']]
    y = df['Temperature']

    # ============================================
    # TRAIN TEST SPLIT
    # ============================================

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # ============================================
    # MODEL TRAINING
    # ============================================

    model = LinearRegression()
    model.fit(X_train, y_train)

    # ============================================
    # PREDICTIONS
    # ============================================

    y_pred = model.predict(X_test)

    # ============================================
    # MODEL EVALUATION
    # ============================================

    st.subheader("📌 Model Evaluation")

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("MAE", f"{mae:.2f}")
        st.metric("RMSE", f"{rmse:.2f}")

    with col2:
        st.metric("MSE", f"{mse:.2f}")
        st.metric("R² Score", f"{r2:.2f}")

    # ============================================
    # ACTUAL VS PREDICTED
    # ============================================

    st.subheader("📉 Actual vs Predicted Temperature")

    fig3, ax3 = plt.subplots(figsize=(12, 5))

    ax3.plot(y_test.values[:100], label="Actual")
    ax3.plot(y_pred[:100], label="Predicted")

    ax3.set_title("Actual vs Predicted Temperature")
    ax3.set_xlabel("Data Points")
    ax3.set_ylabel("Temperature")
    ax3.legend()

    st.pyplot(fig3)

    # ============================================
    # FUTURE TEMPERATURE PREDICTION
    # ============================================

    st.subheader("🔮 Future Temperature Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        future_year = st.number_input(
            "Enter Year",
            min_value=2024,
            max_value=2100,
            value=2026
        )

    with col2:
        future_month = st.number_input(
            "Enter Month",
            min_value=1,
            max_value=12,
            value=6
        )

    with col3:
        future_day = st.number_input(
            "Enter Day",
            min_value=1,
            max_value=31,
            value=15
        )

    if st.button("Predict Temperature"):

        future_data = pd.DataFrame({
            'Year': [future_year],
            'Month': [future_month],
            'Day': [future_day]
        })

        future_prediction = model.predict(future_data)

        st.success(
            f"🌡️ Predicted Temperature: "
            f"{future_prediction[0]:.2f} °C"
        )

    # ============================================
    # SAVE MODEL
    # ============================================

    with open("weather_prediction_model.pkl", "wb") as file:
        pickle.dump(model, file)

    st.success("💾 Model Saved Successfully!")

else:
    st.info("👈 Upload a weather CSV file to begin.")

# ============================================
# FOOTER
# ============================================

st.markdown("---")
st.markdown(
    "Developed using Python, Streamlit, and Machine Learning"
)