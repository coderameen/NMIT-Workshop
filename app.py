import streamlit as st
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
nltk.download('stopwords')
nltk.download('punkt_tab')
stop_words = set(stopwords.words('english'))
def clean_text(text):
    #1. lower case
    text = text.lower()
    #2. Remove Special Symbols
    text = re.sub(r'[^a-zA-Z\s]','',text)
    #3. Remove HTTP links
    text = re.sub(r'https\S','',text)
    #4. Word Tokenize
    tokens = word_tokenize(text)
    #5. removing stop words
    # l = []
    # for word in tokens:
    #     if word not in stop_words:
    #         l.append(word)
    sw_text = [word for word in tokens if word not in stop_words]
    #6. Applying stemming or lemmatization
    # l = []
    # for word in sw_text:
    #     l.append(stemmer.stem(word))
    clean_text = [stemmer.stem(word) for word in sw_text]
    
    return " ".join(clean_text)


#Load Model and Tfidf
import pickle
model = pickle.load(open('model.pkl','rb'))
tfidf = pickle.load(open('tfidf.pkl','rb'))
def fraud_detection(sms):
    sms = clean_text(sms)
    #convert text to number
    features = tfidf.transform([sms])
    pred = model.predict(features)
    if pred.item() == 1:
        return  "Fraud SMS"
    else:
        return "Real SMS"
st.title("SMS Fraud Detection using NLP and ML Techniques")
user_input = st.text_input("Enter SMS to check Real or Fraud!!")\

if st.button("Predict"):
    if user_input:
        res = fraud_detection(user_input)
        st.write(res)
    else:
        st.warning("please enter sms!!!")