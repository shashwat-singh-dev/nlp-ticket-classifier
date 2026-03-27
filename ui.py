import streamlit as st
import requests

st.title("🎫 Ticket Classifier")

text = st.text_input("Enter your issue:")

if st.button("Predict"):
    if text:
        response = requests.get(f"http://127.0.0.1:8000/predict?text={text}")
        
        if response.status_code == 200:
            data = response.json()
            st.success(f"Category: {data['category']}")
            st.info(f"Priority: {data['priority']}")
        else:
            st.error("Error in API")
    else:
        st.warning("Please enter some text")