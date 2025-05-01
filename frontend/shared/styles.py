import streamlit as st
from pathlib import Path

def load_css():
    # Get the path to the styles.css file
    css_file = Path(__file__).parent / 'styles.css'
    
    # Read and load the CSS
    with open(css_file, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 