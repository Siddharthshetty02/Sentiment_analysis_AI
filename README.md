
# Sentiment Analysis AI for Product Reviews

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.2-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.26.0-orange)
![Transformers](https://img.shields.io/badge/Transformers-4.30.2-yellow)

This project is a **full-stack sentiment analysis application** that classifies product reviews as **positive**, **negative**, or **neutral**. It uses a pre-trained **DistilBERT model** for sentiment analysis and provides a user-friendly interface powered by **Streamlit**.

---

## 🚀 Features
- **Sentiment Analysis**: Classifies product reviews into positive, negative, or neutral sentiments.
- **User-Friendly Interface**: Built with Streamlit for easy interaction.
- **Pre-Trained Model**: Uses the `distilbert-base-uncased-finetuned-sst-2-english` model from Hugging Face Transformers.
- **Scalable Backend**: Flask API for handling sentiment analysis requests.

---

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/sentiment-analysis-app.git
   cd sentiment-analysis-app
Set Up the Backend:

Navigate to the backend directory:

bash
Copy
cd backend
Install dependencies:

bash
Copy
pip install -r requirements.txt
Run the Flask API:

bash
Copy
python app.py
The backend will run at http://localhost:5000.

Set Up the Frontend:

Navigate to the frontend directory:

bash
Copy
cd frontend
Install dependencies:

bash
Copy
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
streamlit run streamlit_app.py
The app will open in your browser at http://localhost:8501.

## 🖥️ Usage
Open the Streamlit app in your browser.

Enter a product review in the text box.

Click "Analyze Sentiment".

View the sentiment (positive, negative, or neutral) and confidence score.

## 📂 Project Structure
Copy
sentiment-analysis-app/
├── backend/
│   ├── app.py                # Flask API for sentiment analysis
│   ├── requirements.txt      # Backend dependencies
├── frontend/
│   ├── streamlit_app.py      # Streamlit frontend app
│   ├── requirements.txt      # Frontend dependencies
├── README.md                 # Project documentation
🛠️ Technologies Used
Backend: Flask, Hugging Face Transformers, Python

Frontend: Streamlit

Model: distilbert-base-uncased-finetuned-sst-2-english

## 🤝 Contributing
Contributions are welcome! If you'd like to contribute:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeature).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeature).

Open a pull request.

## 📧 Contact
For questions or feedback, feel free to reach out:
📧 siddharthshetty2032005@gmail.com
🔗 www.linkedin.com/in/siddharth-shetty-657797283
💻 https://github.com/Siddharthshetty02

## Developer 
SIDDHARTH RAGHUNATHA SHETTY
