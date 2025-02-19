import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load datasets
league_data = pd.read_csv("data/league_data.csv")
shortleaf_data = pd.read_csv("data/shortleaf.txt", sep="\t")

st.title("📊 TP 1 Exercises Dashboard")

# -------------------------
# 📌 Exercise 1: League Data Analysis
# -------------------------
st.header("⚽ Exercise 1: League Data Analysis")

st.subheader("Market Value Distribution")
fig, ax = plt.subplots()
sns.histplot(league_data['market_value'], bins=30, kde=True, ax=ax)
st.pyplot(fig)

st.subheader("Market Value vs. Age Category")
fig, ax = plt.subplots()
sns.boxplot(x=league_data['age_cat'], y=league_data['market_value'], ax=ax)
st.pyplot(fig)

# -------------------------
# 📌 Exercise 2: Log-Transformation on Shortleaf Pine Trees
# -------------------------
st.header("🌲 Exercise 2: Log-Transformation on Shortleaf Pine Trees")

st.subheader("Regression Model Performance")
st.text("""
Simple Model      - RMSE: 9.73, R²: 0.8926
Log(Diam) Model   - RMSE: 14.95, R²: 0.7464
Log-Log Model     - RMSE: 0.17, R²: 0.9736
""")

st.subheader("Volume vs. Diameter Regression Line")
fig, ax = plt.subplots()
sns.scatterplot(x=shortleaf_data['Diam'], y=shortleaf_data['Vol'], label="Actual Data", ax=ax)
x_range = np.linspace(shortleaf_data['Diam'].min(), shortleaf_data['Diam'].max(), 100)
y_pred = 6.8367 * x_range - 41.5681  # Example from Linear Regression
ax.plot(x_range, y_pred, color='red', label="Regression Line")
st.pyplot(fig)

# -------------------------
# 📌 Exercise 3: Digits Classification
# -------------------------
st.header("🔢 Exercise 3: Multi-Class Classification")

st.subheader("Confusion Matrix")
conf_matrix = np.array([[35, 0, 0, 1, 0, 0, 0, 0, 0, 0],   # Example from your results
                        [0, 35, 0, 0, 1, 0, 0, 0, 0, 0],  
                        [1, 0, 34, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 36, 0, 0, 0, 0, 0, 1],
                        [0, 1, 0, 0, 35, 0, 0, 0, 0, 0]])
fig, ax = plt.subplots()
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap="Blues")
st.pyplot(fig)

st.subheader("Classification Metrics")
st.text("""
Accuracy: 0.9611
Precision (Macro): 0.9620
Recall (Macro): 0.9607
F1-score (Macro): 0.9607
Precision (Micro): 0.9611
Recall (Micro): 0.9611
F1-score (Micro): 0.9611
""")

st.success("✅ All exercises completed successfully!")
