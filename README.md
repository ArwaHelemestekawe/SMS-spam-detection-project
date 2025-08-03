## 🎬 Demo Video

[![Watch the Demo](https://img.youtube.com/vi/hYiA8QJ77Yk/maxresdefault.jpg)](https://www.youtube.com/watch?v=hYiA8QJ77Yk)


#  Spam Detection App

A simple and interactive web app for detecting spam in SMS or email messages using natural language processing (NLP) and machine learning.

##  Features

- Classifies messages as **Spam** or **Not Spam**
- Shows prediction **probability** using `predict_proba`
- Allows **custom threshold** tuning for decision boundaries
- Built with **Streamlit** for a clean, user-friendly UI
- Uses **NLTK** for advanced text preprocessing


##  Models Used

- `Multinomial Naive Bayes`: excellent at detecting messages with clear spam keywords
- `ExtraTreesClassifier`: more balanced across precision and recall


##  Tech Stack

- **Python 3.10+**
- **Scikit-learn** – for machine learning models
- **NLTK** – for tokenization, stemming, stopwords
- **Streamlit** – for web deployment
- **Pickle** – for saving vectorizer and model artifacts

##  Preprocessing Steps

- Lowercasing input text
- Tokenization using `nltk.word_tokenize`
- Removing stopwords and non-alphanumeric tokens
- Stemming with `PorterStemmer`
- Vectorization via `TfidfVectorizer` (with optional `max_features` tuning)

##  Example Messages

- **Ham**: "Hey, are we still on for dinner?"
- **Spam**: "WIN a FREE vacation now! Click here to claim!"

##  Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/spam-detector-app.git
   cd spam-detector-app
   ```

2. Install requirements  
   ```bash
   pip install -r requirements.txt
   ```

3. Launch Streamlit app  
   ```bash
   streamlit run app.py
   ```

4. Make predictions right from your browser 🎉

##  File Structure

```
├── app.py                  # Streamlit app code
├── model.pickle            # Saved ML model
├── tf.pickle               # Saved vectorizer
├── requirements.txt        # Python dependencies
└── README.md               # Project overview
```

##  About the Developer

Built with care by **Arwa AL_Hashem**

##  License

This project is open-source and free to use under the [MIT License](LICENSE).
```

---

