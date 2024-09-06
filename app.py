# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 21:37:58 2024

@author: mukil
"""

# app.py
from flask import Flask, request, jsonify
import joblib

# Load the model
model = joblib.load('model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
