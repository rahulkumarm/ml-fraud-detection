import streamlit as st
import pandas as pd
import requests

st.title("Fraud Detection System")

uploaded_file = st.file_uploader("Upload your bank statement (CSV)", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV
    df = pd.read_csv(uploaded_file)
    st.write("Here is your uploaded data:")
    st.write(df)
    
    # Send the data to the backend for fraud detection
    response = requests.post("https://your-heroku-backend-url/api/detect", files={"file": uploaded_file})
    
    if response.status_code == 200:
        st.write("Fraudulent transactions detected:")
        st.write(response.json()["fraudulent_transactions"])
    else:
        st.error("Error in processing file")