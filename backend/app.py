from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@app.route('/predict', methods=['POST'])
def predict():
    # Get review text from request
    data = request.json
    review = data.get('review', '')

    if not review:
        return jsonify({'error': 'No review provided'}), 400

    # Perform sentiment analysis
    result = sentiment_pipeline(review)[0]
    sentiment = result['label']
    confidence = result['score']

    # Return result
    return jsonify({
        'review': review,
        'sentiment': sentiment,
        'confidence': confidence
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)