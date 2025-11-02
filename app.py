# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------
st.set_page_config(page_title="Academic Stress Visualization", layout="wide")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
DATA_URL = "https://raw.githubusercontent.com/Nashalan/Assignment-/refs/heads/main/Academic%20Stress%20Level.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

df = load_data()

# detect stress column automatically
def get_stress_column(df):
    for c in df.columns:
        if "stress" in c.lower():
            return c
    return None

stress_col = get_stress_column(df)

# ---------------------------------------------------
# SIDEBAR MENU
# ---------------------------------------------------
st.sidebar.title("📊 Academic Stress Dashboard")
page = st.sidebar.radio(
    "Navigate to:",
    ["🏠 Home", "🎯 Stress Overview", "🎓 Academic Factors", "💬 Social & Support Systems"]
)

# ---------------------------------------------------
# PAGE 1 — HOME
# ---------------------------------------------------
if page == "🏠 Home":
    st.title("🏫 Academic Stress Level Dashboard")
    st.markdown("""
    Welcome to the **Academic Stress Visualization Dashboard**!  
    This dashboard explores how **academic**, **psychological**, and **social factors** influence student stress.

    🔹 **Stress Overview** – General patterns of stress  
    🔹 **Academic Factors** – How study habits and workload affect stress  
    🔹 **Social & Support Systems** – Role of relationships and support in stress reduction
    """)

    st.subheader("📘 Dataset Overview")
    st.dataframe(df.head())

    st.info("👉 Use the sidebar to switch between pages for different insights!")

# ---------------------------------------------------
# PAGE 2 — STRESS OVERVIEW
# ---------------------------------------------------
elif page == "🎯 Stress Overview":
    st.title("🎯 Stress Overview & Patterns")

    st.markdown("### 🎯 Objective")
    st.write("To visualize how stress levels are distributed and identify overall trends across the student population.")

    st.markdown("### 📦 Summary Box")
    st.info("""
    This section shows the overall **distribution** of stress levels 
    and differences across demographic factors such as gender or age.
    """)

    if stress_col:
        # Histogram
        fig1 = px.histogram(df, x=stress_col, nbins=20, color_discrete_sequence=["#4FC3F7"],
                            title="Distribution of Student Stress Levels")
        fig1.update_layout(xaxis_title="Stress Level", yaxis_title="Count")
        st.plotly_chart(fig1, use_container_width=True)

        # Average stress by gender
        if "gender" in df.columns:
            fig2 = px.bar(df, x="gender", y=stress_col, color="gender",
                          title="Average Stress by Gender", barmode="group")
            st.plotly_chart(fig2, use_container_width=True)

        # Stress vs Age
        if "age" in df.columns:
            fig3 = px.line(df.sort_values("age"), x="age", y=stress_col,
                           title="Stress Level Trend by Age", markers=True)
            st.plotly_chart(fig3, use_container_width=True)

        st.markdown("### 💬 Interpretation")
        st.success("""
        Most students fall within moderate stress levels.  
        Differences between genders or ages reveal how various groups experience stress uniquely, 
        helping institutions target support efforts effectively.
        """)
    else:
        st.error("No stress column found in dataset.")

# ---------------------------------------------------
# PAGE 3 — ACADEMIC FACTORS
# ---------------------------------------------------
elif page == "🎓 Academic Factors":
    st.title("🎓 Academic Factors Influencing Stress")

    st.markdown("### 🎯 Objective")
    st.write("To explore how academic workload, study time, and performance are linked to students' stress levels.")

    st.markdown("### 📦 Summary Box")
    st.info("""
    Academic pressure plays a significant role in student stress.
    This section analyzes how factors such as **study hours**, **course difficulty**, and **grades**
    correlate with stress using interactive visuals.
    """)

    if stress_col:
        # Correlation with stress
        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        if stress_col in numeric_cols:
            corr = df[numeric_cols].corr()[stress_col].sort_values(ascending=False).reset_index()
            corr.columns = ['Variable', 'Correlation with Stress']
            fig_corr = px.bar(corr, x='Variable', y='Correlation with Stress',
                              color='Correlation with Stress', color_continuous_scale='RdBu',
                              title="Correlation Between Academic Variables and Stress")
            st.plotly_chart(fig_corr, use_container_width=True)

        # Scatter of user choice
        academic_cols = [c for c in df.columns if "study" in c or "grade" in c or "course" in c]
        if academic_cols:
            x_var = st.selectbox("Select an Academic Variable:", academic_cols)
            fig = px.scatter(df, x=x_var, y=stress_col, color=stress_col,
                             color_continuous_scale="Inferno", trendline="ols",
                             title=f"{x_var.replace('_',' ').title()} vs Stress Level")
            st.plotly_chart(fig, use_container_width=True)

        # Mean stress by academic variable
        if "course_load" in df.columns:
            avg_stress = df.groupby("course_load")[stress_col].mean().reset_index()
            fig_bar = px.bar(avg_stress, x="course_load", y=stress_col, color=stress_col,
                             title="Average Stress by Course Load")
            st.plotly_chart(fig_bar, use_container_width=True)

        st.markdown("### 💬 Interpretation")
        st.success("""
        Academic workload and grades show a direct relationship with stress.  
        Heavy course loads or long study hours often correlate with higher stress, 
        while balanced workloads are associated with lower stress levels.
        """)
    else:
        st.error("No stress column found in dataset.")

# ---------------------------------------------------
# PAGE 4 — SOCIAL & SUPPORT SYSTEMS
# ---------------------------------------------------
elif page == "💬 Social & Support Systems":
    st.title("💬 Social & Support Systems & Stress")

    st.markdown("### 🎯 Objective")
    st.write("To examine how social interactions, friendships, and emotional support affect students’ stress levels.")

    st.markdown("### 📦 Summary Box")
    st.info("""
    Support systems — friends, family, and mentors — can significantly reduce stress.
    This section visualizes how social engagement and emotional support levels relate to student stress.
    """)

    if stress_col:
        # 1. Social support vs stress
        if "social_support" in df.columns:
            fig1 = px.scatter(df, x="social_support", y=stress_col, color=stress_col,
                              color_continuous_scale="Tealrose", trendline="ols",
                              title="Social Support vs Stress Level")
            st.plotly_chart(fig1, use_container_width=True)

        # 2. Friend interaction vs stress
        if "friend_interaction" in df.columns:
            fig2 = px.box(df, x="friend_interaction", y=stress_col, color="friend_interaction",
                          title="Stress Levels Across Friendship Interaction Frequency")
            st.plotly_chart(fig2, use_container_width=True)

        # 3. Combined 3D View (if variables exist)
        if all(c in df.columns for c in ["social_support", "friend_interaction"]):
            fig3 = px.scatter_3d(df, x="social_support", y="friend_interaction", z=stress_col,
                                 color=stress_col, color_continuous_scale="Viridis",
                                 title="3D Relationship: Social Support, Friendship & Stress")
            st.plotly_chart(fig3, use_container_width=True)

        st.markdown("### 💬 Interpretation")
        st.success("""
        Students with **strong social support** and **frequent social interactions**
        generally report **lower stress levels**.  
        The 3D plot shows that combining emotional support and active friendships 
        creates the lowest stress zones — emphasizing the power of community support.
        """)
    else:
        st.error("No stress column found in dataset.")
