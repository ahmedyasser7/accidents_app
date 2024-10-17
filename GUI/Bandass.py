import nbformat
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from openpyxl import load_workbook
import plotly.express as px
from nbconvert import PythonExporter
import pickle

################################
# Main app structure
st.set_page_config(page_title="Bandaas", layout="wide", page_icon= r"https://github.com/ahmedyasser7/accidents_app/blob/main/GUI/images/two_cars.png")

@st.cache_resource
def load_image(image_path):
    return Image.open(image_path)

################################
@st.cache_resource
def page_image_display():
    st.title("LOOK OUT!!!")
    image = load_image(r"GUI\images\two_cars.png")
    st.image(image, caption="We are a collabortive Team!")

################################
@st.cache_resource
def Page_overview():
    st.title("Overview")
    st.write(f"The link for the GitHub Repo")
    st.write(f"The link for the Documentation")
    st.write(f"The link for the Presentation")


################################
@st.cache_resource
def page_authors():
    st.title("Teammates")
    st.write("## Names")
    st.write("""
    - Ahmed Yasser 
    - Ahmed Abd El-Hameed (7ameedo)
    - Abram Maher
    - Sarah Mohammed Selim
    - Naglaa Reda
    """)
    st.write(" We wish you enjoy this journey!")

################################
Bandass_PAGES = {
    "Hello": page_image_display,
    "Overview": Page_overview,
    "Team Names": page_authors,
}

################################
def main():
    selection = st.radio("", list(Bandass_PAGES.keys()), index=0)
    page = Bandass_PAGES[selection]
    page()

if __name__ == "__main__":
    main()
