""" 
This is the making of a streamlit app for the best choice of crop 
"""

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import joblib
from templates import home_page, geek_page, pred_direct, pred_real_time, pred_by_data, stats_price

# Load the model with error handling
try:
    best_model = joblib.load("rf_model.joblib")
except FileNotFoundError:
    st.error("Model file not found. Please check the file path.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()

def home():

    col1, col2, col3 = st.columns(3)
    with col1:
     st.write(' ')  # Empty column
    with col2:
     st.title("Farma.AI")
    with col3:
     st.write(' ')

    option = st.selectbox(
        'Select an option',
        ['Choose your option', 'Direct Crop Prediction', 'Real-time Crop Prediction', 'Real-time Crop Prediction with previous soil data']
    )

    if option == 'Choose your option':
        home_page()
    elif option == 'Direct Crop Prediction':
        pred_direct(best_model)
    elif option == 'Real-time Crop Prediction':
        pred_real_time(best_model)
    elif option == 'Real-time Crop Prediction with previous soil data':
        pred_by_data(best_model)

# Define the pages
def pricing():
    stats_price()

def expert():
    geek_page()


# Create a top navigation bar
selected = option_menu(
    menu_title=None,  # No title for the menu
    options=["Home", "Pricing", "Expert"],  # Options for the menu
    icons=["house", "currency-exchange", "person"],  # Icons for each option
    menu_icon="cast",  # Menu icon
    default_index=0,  # Default index for the menu
    orientation="horizontal"  # Set orientation to horizontal for top navigation
)

# Display the selected page
if selected == "Home":
    home()
elif selected == "Pricing":
    pricing()
elif selected == "Expert":
    expert()