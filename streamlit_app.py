# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 21:38:13 2024

@author: mukil
"""

# streamlit_app.py
# import streamlit as st
# import requests

# st.title("ML Model Deployment")

# # Input form
# sepal_length = st.number_input('Sepal Length', value=5.0)
# sepal_width = st.number_input('Sepal Width', value=3.0)
# petal_length = st.number_input('Petal Length', value=1.5)
# petal_width = st.number_input('Petal Width', value=0.2)

# # Prediction button
# if st.button('Predict'):
#     data = {
#         'features': [sepal_length, sepal_width, petal_length, petal_width]
#     }
#     response = requests.post('http://127.0.0.1:5000/predict', json=data)
#     result = response.json()
#     st.write(f"Prediction: {result['prediction']}")

import streamlit as st
import requests

# Title of the app
st.title("Iris Flower Classification Model")

# Input form for features
sepal_length = st.number_input('Sepal Length', value=5.0)
sepal_width = st.number_input('Sepal Width', value=3.0)
petal_length = st.number_input('Petal Length', value=1.5)
petal_width = st.number_input('Petal Width', value=0.2)

# Button to trigger prediction
if st.button('Predict'):
    # Prepare the input data for the API
    data = {
        'features': [sepal_length, sepal_width, petal_length, petal_width]
    }
    
    # Send a request to the Flask API
    try:
        response = requests.post('http://127.0.0.1:5000/predict', json=data)
        result = response.json()
        st.write(f"Prediction: {result['prediction']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: Could not connect to the prediction service. {e}")