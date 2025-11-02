import streamlit as st
import pandas as pd

st.set_page_config(page_title="Academic Stress Level Dashboard", layout="wide")

# ------------------------
# Load Dataset
# ------------------------
DATA_URL = "https://raw.githubusercontent.com/Nashalan/Assignment-/refs/heads/main/Academic%20Stress%20Level.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    # Clean column names for consistency
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

df = load_data()

# ------------------------
# Main Page
# ------------------------
st.title("📊 Academic Stress Level Dashboard")
st.markdown("""
Welcome to the **Academic Stress Level Visualization App**.  
This dashboard explores how students experience academic stress and the factors that influence it.

### 📘 Pages
- **Stress Level Distribution:** Explore the spread of stress levels.  
- **Academic Factors & Stress:** See how grades and study hours affect stress.  
- **Lifestyle Factors & Stress:** Understand how sleep and activity impact stress.

Dataset Source:  
[Academic Stress Level.csv](https://raw.githubusercontent.com/Nashalan/Assignment-/refs/heads/main/Academic%20Stress%20Level.csv)
""")

st.write("### 🧾 Dataset Preview")
st.dataframe(df.head())

st.write("### 📑 Columns in the Dataset")
st.write(df.columns.tolist())
