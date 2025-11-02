import streamlit as st
import pandas as pd

st.set_page_config(page_title="Academic Stress Level Dashboard", layout="wide")

st.title("📊 Academic Stress Level Dashboard")
st.markdown("""
Welcome to the **Academic Stress Level Visualization App**.  
This dashboard explores how stress levels vary among students and the factors that influence them.

### 📘 Pages
- **Stress Level Distribution:** Explore how stress varies among students.  
- **Academic Factors & Stress:** Examine how academic variables like GPA or study hours relate to stress.  
- **Lifestyle Factors & Stress:** Discover how sleep and physical activity impact stress.

The dataset used is from:
[Academic Stress Level.csv](https://raw.githubusercontent.com/Nashalan/Assignment-/refs/heads/main/Academic%20Stress%20Level.csv)
""")

# Load and preview data
DATA_URL = "https://raw.githubusercontent.com/Nashalan/Assignment-/refs/heads/main/Academic%20Stress%20Level.csv"
@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)

df = load_data()

st.subheader("📂 Dataset Preview")
st.dataframe(df.head())
