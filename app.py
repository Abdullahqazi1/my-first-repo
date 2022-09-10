import streamlit as st
from survey_result import show_survey_result

st.sidebar.selectbox("Explor" or "Predict", ("Predict", "Explore"))

show_survey_result()