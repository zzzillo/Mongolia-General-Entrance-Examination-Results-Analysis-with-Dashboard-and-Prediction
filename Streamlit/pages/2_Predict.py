import streamlit as st
import pandas as pd
import joblib
from statsmodels.distributions.empirical_distribution import ECDF

df = pd.read_csv("Streamlit/Combined Dataset.csv")
model = joblib.load("Streamlit/rf_percentile_model.pkl")

st.markdown("""
    <div style="background-color:#113f67;padding:15px;margin:-2rem -1rem 2rem -1rem;color:#58a0c8">
        <h1 style="color:#e6f6ff;text-align:center;font-size:36px">Mongolian General Entrance Exam Results Results Predict Percentile</h1>
    </div>
""", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["Predict Converted Score Percentile", "Predict First Score Percentile by Subject"])

with tab1:
    st.markdown("<h3 style='text-align:center; color:#113f67;'>Predict Percentile using Converted Score</h3>", unsafe_allow_html=True)
    converted_score = st.number_input("Enter Converted Score (200–800):", min_value=200, max_value=800, step=1)
    prediction = None  
    col1, col2, col3 = st.columns([7, 4, 6])
    with col2:
        if st.button("Predict Percentile", key="ml_predict"):
            input_df = pd.DataFrame({"Convertedscore": [converted_score]})
            prediction = model.predict(input_df)[0]
    if prediction is not None:
        st.success(f"Predicted Percentile: **{prediction:.4f}**%")

with tab2:
    st.markdown("<h3 style='text-align:center; color:#113f67;'>Predict Percentile using First Score and Subject</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        subject_list = sorted(df["Subject"].dropna().unique())
        subject = st.selectbox("Select Subject:", subject_list)

    with col2: 
        first_score = st.number_input("Enter First Score (0–100):", min_value=0, max_value=100, step=1)
    col3, col4, col5 = st.columns([7, 4 , 6])
    percentile_result = None
    error_flag = False

    with col4:
            if st.button("Predict Percentile", key="ecdf_predict"):
                subject_scores = df[df["Subject"] == subject]["Firstscore"].dropna()
                if subject_scores.empty:
                    error_flag = True
                else:
                    ecdf = ECDF(subject_scores)
                    percentile_result = ecdf(first_score) * 100

        # Show result or error after the button row
    if error_flag:
        st.error("No data for this subject.")
    elif percentile_result is not None:
        st.success(f"Predicted Percentile: **{percentile_result:.2f}**%")
