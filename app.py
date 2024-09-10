import streamlit as st
import pickle

with open('spam_detection_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorization = pickle.load(vectorizer_file)

st.title("Spam Mail Classifier")

user_input = st.text_area("Enter the mail text")

if st.button('Classify Mail'):
    if user_input.strip() != "":
        user_input_v = vectorization.transform([user_input])

        prediction = model.predict(user_input_v)

        if prediction[0] == 1:
            st.success("Not a spam mail")
        else:
            st.error("Spam mail detected")
    else:
        st.warning("Please enter your mail.")
