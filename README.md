# 📩 Spam Detection App

A simple and interactive web app for detecting spam in SMS or email messages using natural language processing (NLP) and machine learning.

## 🔍 Features

- Classifies messages as **Spam** or **Not Spam**
- Shows prediction **probability** using `predict_proba`
- Built with **Streamlit** for a clean, user-friendly UI
- Uses **NLTK** for advanced text preprocessing


## 🧠 Models Used

- `Multinomial Naive Bayes`: excellent at detecting messages with clear spam keywords
- `ExtraTreesClassifier`: more balanced across precision and recall
## 🔧 Tech Stack

- **Python 3.10+**
- **Scikit-learn** – for machine learning models
- **NLTK** – for tokenization, stemming, stopwords
- **Streamlit** – for web deployment
- **Pickle** – for saving vectorizer and model artifacts

## 🧪 Preprocessing Steps

- Lowercasing input text
- Tokenization using `nltk.word_tokenize`
- Removing stopwords and non-alphanumeric tokens
- Stemming with `PorterStemmer`
- Vectorization via `TfidfVectorizer` (with optional `max_features` tuning)

## 🖼 Example Messages

- **Ham**: "Hey, are we still on for dinner?"
- **Spam**: "WIN a FREE vacation now! Click here to claim!"

## 🚀 Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/spam-detector-app.git
   cd spam-detector-app
