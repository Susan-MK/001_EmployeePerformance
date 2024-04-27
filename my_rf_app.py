# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19To9jFHAmz1rYObJPWoKH9V454G5kAtw

## Streamlit Employee Performance Web App
"""

#install streamlit if not already installed
#!pip install streamlit

# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import pickle
st.set_option('deprecation.showPyplotGlobalUse', False)

# Define the main function to train and evaluate the model
def main():
    st.title("Random Forest Classifier App")

    # Upload dataset
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        st.write("### Dataset Preview")
        df = pd.read_csv(uploaded_file)
        st.write(df.head())

        # Split dataset into features and target variable
        X = df.drop(columns=['PerformanceRating'])
        y = df['PerformanceRating']

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train Random Forest Classifier
        clf = RandomForestClassifier(random_state=42)
        clf.fit(X_train, y_train)

        # Make predictions
        y_pred = clf.predict(X_test)

        # Evaluate model
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        confusion = confusion_matrix(y_test, y_pred)

        # Display evaluation metrics
        st.write("### Evaluation Metrics")
        st.write(f"Test Accuracy: {accuracy:.3f}")
        st.write("Classification Report:")
        st.write(report)
        st.write("Confusion Matrix:")
        st.write(confusion)

# Run the main function
if __name__ == "__main__":
    main()