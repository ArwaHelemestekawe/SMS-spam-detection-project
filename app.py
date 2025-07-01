import streamlit as st
import pickle
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize

nltk.data.path.append("C:/nltk_data")
nltk.data.path.append("C:/stop_word_data") 


ps = PorterStemmer()
stop_words = set(stopwords.words('english'))  # only once

def pre_text(text_in):
    text = text_in.lower()
    tokens = nltk.word_tokenize(text)
    final_list = []

    for word in tokens:
        if word.isalnum() and word not in stop_words:
            final_list.append(ps.stem(word))

    return " ".join(final_list)




tf=pickle.load(open("tf.pickle","rb"))
model=pickle.load(open("model.pickle","rb"))



st.header("Email & SMS spam detection")
message=st.text_area("Enter the message ")


transformed_text=pre_text(message)
tf_text=tf.transform([transformed_text])


result=model.predict(tf_text)[0]
probability=model.predict_proba(tf_text)
if st.button("predict"):
  st.header(probability)
  
  if probability[0][1]>=0.40:
      st.header("spam")
     


      

  elif result==0:
    st.header("not a spam")

    




# process > vectorize > predict 



st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        /* or try background-image: url("your-image-url"); */
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.markdown(
    """
    <style>
    h1, h2, h3, h4, h5, h6 {
        color: red !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)