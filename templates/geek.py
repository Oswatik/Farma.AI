import streamlit as st
import pandas as pd
from PIL import Image

def geek_page():
    # Different algorithms for models
    data = model_selection = {
        'accuracy' : [0.989, 0.995, 0.958, 0.995, 0.991, 0.993, 0.985],
        'model' : ['DecisionTree', 'NaiveBayes', 'LogisticRegression', 'RandomForest', 'XgBoost', 'LightGBM', 'SVM']
    }
    df = pd.DataFrame(data)

    st.header("Latest model testing charts")
    # Plot the bar chart
    st.bar_chart(df, x="model", y="accuracy")
    st.write("Random Forest has been chosen as the the model for this problem with an accuracy of 99.5%.")

    st.write("The Data has been gathered from https://data.gov.in/catalogs?sector=Agriculture")
    image = Image.open('Images/green.jpg')
    st.image(image)