import streamlit as st
import matplotlib.pyplot as plt
from model import predict_risk
from rag_engine import get_answer
from genai_helper import enhance_response

# Page configuration.....
st.set_page_config(page_title="Health Risk Prediction", layout="wide")

# Ui style 
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background-color: #eef2f7;
    font-family: 'Poppins', sans-serif;
}

/* MAIN CARD */
.block-container {
    background: #f8fbff;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(135deg, #36d1dc, #5b86e5);
    color: white;
    border-radius: 12px;
    height: 45px;
    width: 100%;
    border: none;
    font-size: 16px;
    font-weight: bold;
}

/* INPUT */
input, .stNumberInput input {
    border-radius: 10px !important;
    border: 1px solid #ccc;
}

/* SIDEBAR LIGHT COLOR */
section[data-testid="stSidebar"] {
    background-color: #e3ecff;
    color: #2c3e50;
}

/* SIDEBAR TEXT */
section[data-testid="stSidebar"] * {
    color: #2c3e50 !important;
}

/* METRIC BOX */
[data-testid="metric-container"] {
    background-color: #eaf0ff;
    border-radius: 12px;
    padding: 10px;
}

/* TEXT */
p, label {
    color: #2c3e50;
}

</style>
""", unsafe_allow_html=True)

#Main Heading......
st.markdown("""
<h1 style="
text-align:center;
font-size:42px;
font-weight:800;
color:#4a90e2;
">
🧠 Health Risk Prediction & Analytics System
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center; color:#34495e; font-size:18px;">
AI-powered health insights for better decision making
</p>
""", unsafe_allow_html=True)

st.divider()

#Side bar 
menu = st.sidebar.radio("📌 Navigation", ["Health Analysis", "AI Chatbot"])


# 🧪 HEALTH ANALYSIS

if menu == "Health Analysis":

    st.markdown("""
    <h2 style="color:#4a90e2; font-weight:700;">
    🧪 Enter Patient Details
    </h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1)
        bmi = st.number_input("BMI", min_value=10.0)

    with col2:
        glucose = st.number_input("Glucose Level", min_value=50)
        bp = st.number_input("Blood Pressure", min_value=50)

    st.write("")

    if st.button("🔍 Analyze Health"):
        percentage, level = predict_risk(age, bmi, glucose, bp)

        st.divider()
        st.markdown("### 📊 Analysis Result")

        c1, c2 = st.columns(2)
        c1.metric("Risk Level", level)
        c2.metric("Risk Percentage", f"{percentage}%")

        if level == "High Risk":
            st.error("⚠️ High risk detected. Please consult a doctor.")
        else:
            st.success("✅ You are in safe range. Maintain healthy lifestyle.")

        st.info("📍 In India, lifestyle diseases like diabetes and BP are increasing.")

        # Graph
        st.divider()
        st.markdown("### 📈 Health Factors Analysis")

        labels = ["Age", "BMI", "Glucose", "BP"]
        values = [age, bmi, glucose, bp]

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_title("Health Parameters Overview")
        ax.set_xlabel("Factors")
        ax.set_ylabel("Values")

        st.pyplot(fig)


# 💬 AI CHATBOT

elif menu == "AI Chatbot":

    st.markdown("""
    <h2 style="color:#4a90e2; font-weight:700;">
    💬 GenAI Healthcare Assistant
    </h2>
    """, unsafe_allow_html=True)

    query = st.text_input("Ask your health question:")

    if st.button("🧠 Get AI Response"):
        base = get_answer(query)
        final = enhance_response(query, base)

        st.divider()
        st.markdown("### 🧠 AI Insight")
        st.info(final)