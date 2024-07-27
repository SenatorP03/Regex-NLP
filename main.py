# import necessary libraries
import glob
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
import streamlit as st

# create a sentiment analysizer instance
analysizer = SentimentIntensityAnalyzer()

# get the name of documents in the folder
doc = glob.glob('diary/*.txt')

# create a dictionary for both group of expected dataset (positive and negative scores or rating)
negative = {}
positive = {}

# re-iterate over the items in folder and store in a variable
for item in doc:
    with open(item ,"r", encoding = "UTF-8") as file:
        text = file.read()

# get the sentiment analysis of each file in folder and categorize output in each dictionary
    scores = analysizer.polarity_scores(text)
    positive.update({item[6:16]: scores["pos"]})
    negative.update({item[6:16]: scores["neg"]})

# build the app
st.title("Dairy tone")
st.subheader("Postivity")
pos_fig = px.line(x=positive.keys(),y=positive.values(),
                  labels={"x":"Date","y": "Positivity"})
st.plotly_chart(pos_fig)
st.subheader("Negativiy")
pos_fig_n= px.line(x=negative.keys(),y=negative.values(),
                  labels={"x":"Date","y": "Negative"})
st.plotly_chart(pos_fig_n)