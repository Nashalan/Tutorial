import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("🎓 Objective 2: Academic Factors & Stress")
st.markdown("**Objective Statement:** To examine how academic performance and workload influence stress levels.")

st.info("""
**Summary:**  
This section explores how academic variables like GPA and study hours relate to stress levels.  
Understanding these relationships helps identify whether workload and performance pressure increase stress.
""")

# Load data
DATA_URL = "https://raw.githubusercontent.com/Nashalan/Assignment-/refs/heads/main/Academic%20Stress%20Level.csv"
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

df = load_data()

# Choose variable
numeric_cols = df.select_dtypes(include='number').columns.tolist()
x_axis = st.selectbox("Select an academic variable to compare with stress level:", numeric_cols, index=0)

# Visualization 1: Scatter Plot
st.subheader(f"1️⃣ Scatter Plot: {x_axis} vs Stress Level")
fig = px.scatter(df, x=x_axis, y='stress_level', trendline="ols", color_discrete_sequence=['teal'])
st.plotly_chart(fig)

# Visualization 2: Correlation Heatmap
st.subheader("2️⃣ Correlation Heatmap")
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Visualization 3: Pairplot
academic_vars = [c for c in ['gpa', 'study_hours', 'stress_level'] if c in df.columns]
if len(academic_vars) >= 2:
    sns.pairplot(df[academic_vars], diag_kind="kde")
    st.pyplot(plt.gcf())

st.success("""
**Interpretation:**  
These visuals show how academic stress relates to academic workload and performance.  
Higher study hours may increase stress, while higher GPA might reduce it — guiding educators to balance workloads.
""")
