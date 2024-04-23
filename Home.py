import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    layout='wide'
)

st.write("# Major Prediction Using Machine Learning")

image = Image.open('MachineLearning.png')
left, right = st.columns([3,1])
right.image(image, use_column_width=True)

left.write("""
This app predicts the user's best-fit academic major category using the answers to the **HEXACO Personality Inventory**. 
           
The HEXACO Personality Inventory describes personality in six different domains: **H**onesty-Humility, **E**motionality, e**X**traversion, **A**greeableness, **C**onscientiousness, and **O**penness to Experience.
Each of these domains has four more specific facets within them. Domain-level and facet-level scores can be viewed after taking the survey.
         
Majors have been separated into 8 categories: 
**Humanities**, **Visual and Performing Arts**, **Social Sciences**, **Business**, **Physical Sciences / Mathematics**, **Engineering**, **Biological Sciences**, and **Health Sciences**.
To see how each UA major has been separated into one of these categories, click the button below.""")

if left.button("UA Majors"):
    st.switch_page("pages/4_UAMajors.py")

left.write("This app uses a machine learning model to make predictions. These predictions are based on data collected from the online HEXACO Personality Inventory through self-reported answers and major categories.")

if left.button("Begin survey"):
    st.switch_page("pages/1_Survey.py")
