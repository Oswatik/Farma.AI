import streamlit as st
from PIL import Image

def home_page():
    image = Image.open('Images/farm-field.jpg')
    st.image(image)
    st.header("About Us")
    st.write("Welcome to Farma.AI! A Pharma for farms, a portal created for helping farmers and agricultural buisness owners to make educated advancement in their fields and ensuring their crop safety by planing correctly. It takes into account the different locations, soil types and rainfall parameters across whole country of India to help farmers make their best bets on their crops. It offers three ways of prediction for choice of crops, the first one fully relying on mannual information given by the customer, the second getting based on real-time weather forcasting and third one being estimated by past data of the area. The service also offers pricing functionality over different regions of the country. People can also check out our expert opinion on expert page.")
    st.subheader("Authors")
    st.write("Created by Anachaser")
    


    