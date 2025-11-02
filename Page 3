import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("💤 Objective 3: Lifestyle Factors & Stress")
st.markdown("**Objective Statement:** To explore how sleep duration and physical activity influence stress levels.")

st.info("""
**Summary:**  
This section explores lifestyle variables such as sleep and exercise to determine their role in stress management.  
Students with healthier lifestyles may experience lower academic stress.
""")

# Load dataset
DATA_URL = "https://raw.githubusercontent.com/Nashalan/Assignment-/refs/heads/main/Academic%20Stress%20Level.csv"
@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)

df = load_data()

# Visualization 1: Sleep vs Stress
if 'Sleep Duration' in df.columns:
    st.subheader("1️⃣ Sleep Duration vs Stress Level")
    fig = px.scatter(df, x='Sleep Duration', y='Stress Level', color='Sleep Duration', color_continuous_scale='viridis')
    st.plotly_chart(fig)

# Visualization 2: Physical Activity vs Stress
if 'Physical Activity' in df.columns:
    st.subheader("2️⃣ Stress Level by Physical Activity")
    fig, ax = plt.subplots()
    sns.boxplot(x='Physical Activity', y='Stress Level', data=df, palette='coolwarm', ax=ax)
    st.pyplot(fig)

# Visualization 3: 3D Scatter
if all(x in df.columns for x in ['Sleep Duration', 'Physical Activity', 'Stress Level']):
    st.subheader("3️⃣ 3D Plot: Sleep, Activity & Stress")
    fig = px.scatter_3d(df, x='Sleep Duration', y='Physical Activity', z='Stress Level', color='Stress Level')
    st.plotly_chart(fig)

st.success("""
**Interpretation:**  
The visualizations show how healthy habits such as enough sleep and regular physical activity 
can help lower academic stress. Promoting these behaviors could improve students’ well-being.
""")
