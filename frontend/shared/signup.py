import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def signup_page():
    st.title("Sign Up")
    
    with st.form("signup_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        role = st.selectbox("Role", ["Student", "Teacher"])
        submit = st.form_submit_button("Sign Up")
        
        if submit:
            # TODO: Implement signup logic
            st.success("Sign up functionality will be implemented soon!")

    st.markdown("""
        <p class="auth-footer">
            Already have an account? <a href="?page=login" class="auth-link">Login here</a>
        </p>
    """, unsafe_allow_html=True) 