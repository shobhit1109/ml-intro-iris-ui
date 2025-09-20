#Deploy the model - iris_model.pkl ( Streaming app using Streamlit)

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the model
model = joblib.load('iris_model.pkl')

# Title of the app
st.title("Iris Flower Species Prediction")
st.write("Enter the features of the iris flower to predict its species.")
# Input features
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0)
# Predict button
if st.button("Predict"):
    # Create a DataFrame for the input features
    input_data = pd.DataFrame({
        'SepalLengthCm': [sepal_length],
        'SepalWidthCm': [sepal_width],
        'PetalLengthCm': [petal_length],
        'PetalWidthCm': [petal_width]
    })
    # Make prediction
    prediction = model.predict(input_data)
    # Map the prediction to species name
    species_map = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}
    predicted_species = species_map[prediction[0]]
    # Display the result
    st.success(f"The predicted species is: {predicted_species}")
# To run the app, use the command: streamlit run app.py
