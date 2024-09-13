# Spam-Detector

A web app that utilizes machine learning algorithms to classify emails and messages as spam or not, providing
accurate and efficient filtering to manage and organize communications

## Features
Spam Detection: The model classifies emails into "Spam" or "Not Spam" based on the input text.
TF-IDF Vectorization: Transforms the text data into numerical format for the model.
Streamlit Integration: The app is built using the Streamlit framework, allowing users to input email text and get predictions in real time.

## Model Training

The spam classification model is built using the following steps:

Data Preprocessing: Email messages are vectorized using TF-IDF (Term Frequency - Inverse Document Frequency).
Model: A Logistic Regression model is trained using the transformed data.
Accuracy: The model achieves an accuracy of approximately 96.77% on the test set.

## Files in the Repository

spam_detection_model.pkl: The trained model.
vectorizer.pkl: The fitted TF-IDF vectorizer used to transform email texts.
app.py: The main Streamlit application for classifying user input.
mails.csv: The dataset used for training and testing the model.

