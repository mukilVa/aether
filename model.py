# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# model.py
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
data = load_iris()
X, y = data.data, data.target

# Train a simple model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, 'model.pkl')
