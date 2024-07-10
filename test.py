## This page is not related to the workflow
## It was created for checking if Streamlit is working properly. You can also run this to check the working of this simple streamlit app.

import streamlit as st
from streamlit_option_menu import option_menu

# Define the pages
def home():
    st.title("Home Page")
    st.write("Welcome to the home page!")

def about():
    st.title("About Page")
    st.write("This is the about page.")

def contact():
    st.title("Contact Page")
    st.write("This is the contact page.")

# Create a top navigation bar
selected = option_menu(
    menu_title=None,  # No title for the menu
    options=["Home", "About", "Contact"],  # Options for the menu
    icons=["house", "info", "envelope"],  # Icons for each option
    menu_icon="cast",  # Menu icon
    default_index=0,  # Default index for the menu
    orientation="horizontal"  # Set orientation to horizontal for top navigation
)

# Display the selected page
if selected == "Home":
    home()
elif selected == "About":
    about()
elif selected == "Contact":
    contact()



