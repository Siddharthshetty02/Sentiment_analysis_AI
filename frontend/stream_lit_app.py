import streamlit as st
import requests

# Title of the app
st.title("Product Review Sentiment Analysis")

# Input text box for user to enter review
review = st.text_area("Enter your product review here:")

# Button to trigger sentiment analysis
if st.button("Analyze Sentiment"):
    if review:
        # Send request to Flask API
        response = requests.post(
            'http://localhost:5000/predict',
            json={'review': review}
        )

        if response.status_code == 200:
            result = response.json()
            st.success(f"Sentiment: {result['sentiment']}")
            st.info(f"Confidence: {result['confidence']:.2f}")
        else:
            st.error("Error analyzing sentiment. Please try again.")
    else:
        st.warning("Please enter a review to analyze.")