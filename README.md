# 🌦️ Weather Data Analysis and Prediction System

A Machine Learning-based Weather Forecasting project built using Python and Streamlit.  
This project analyzes historical weather data and predicts future temperature trends using Linear Regression.

---

# 📌 Features

- 📂 Upload Weather CSV Dataset
- 📊 Weather Data Analysis
- 📈 Temperature Trend Visualization
- 📉 Actual vs Predicted Graph
- 🤖 Machine Learning Prediction
- 🔮 Future Temperature Forecasting
- 💾 Save Trained Model
- 🌐 Interactive GUI using Streamlit

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit

---

# 📂 Project Structure

```text
Weather-Prediction/
│
├── app.py
├── weather.csv
├── requirements.txt
├── weather_prediction_model.pkl
└── README.md
```
# 📊 Dataset Format

Your CSV file should contain the following columns:

```csv
Date,Temperature,Humidity,WindSpeed,Pressure
2024-01-01,25,60,10,1012
2024-01-02,26,62,12,1011
2024-01-03,24,58,8,1015
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone <your-github-repo-link>
cd Weather-Prediction
```

---

## 2️⃣ Create Virtual Environment (Optional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🌐 Streamlit App Features

## 📂 Dataset Upload

Upload your weather CSV file directly from the GUI.

---

## 📈 Temperature Trend Analysis

Visualize historical temperature changes.

---

## 📊 Monthly Average Analysis

Analyze monthly weather patterns.

---

## 🤖 Machine Learning Model

Uses Linear Regression for prediction.

---

## 🔮 Future Temperature Prediction

Predict temperature for any future date.

---

## 📉 Model Evaluation

Displays:

- MAE
- MSE
- RMSE
- R² Score

---

# 🧠 Machine Learning Workflow

1. Data Collection  
2. Data Cleaning  
3. Feature Engineering  
4. Exploratory Data Analysis  
5. Model Training  
6. Prediction  
7. Evaluation  

---

# 📷 Output Screens

You can add screenshots here later:

```text
screenshots/
│
├── dashboard.png
├── prediction.png
└── graph.png
```

---

# 📦 Required Libraries

```txt
streamlit
pandas
numpy
matplotlib
scikit-learn
openpyxl
```

---

# 🚀 Future Improvements

- 🌦️ Live Weather API Integration
- 🧠 Deep Learning using LSTM
- 📊 Interactive Graphs using Plotly
- ☁️ Cloud Deployment
- 📱 Mobile Responsive Dashboard
- 📥 Download Prediction Reports

---

# 📚 Learning Outcomes

Through this project you will learn:

- Data Analysis
- Data Visualization
- Machine Learning Basics
- Regression Algorithms
- Streamlit GUI Development
- Model Evaluation Techniques

---

# 🧪 Sample Prediction

```text
Input Date: 15-06-2026
Predicted Temperature: 34.5 °C
```

---

# 👨‍💻 Author

**Vikas Thapa**  
M.Sc Computer Science Student  

---

# 📜 License

This project is open-source and free to use for educational purposes.