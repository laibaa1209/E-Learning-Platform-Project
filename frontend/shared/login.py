import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def login_page():
    st.markdown("""
        <div class="auth-container">
            <h1 class="auth-title">Welcome Back!</h1>
            <p class="auth-subtitle">Sign in to continue your learning journey</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Role selection using Streamlit components
    st.markdown("<h3 style='text-align: center; color: rgba(255,255,255,0.7);'>Select your role</h3>", unsafe_allow_html=True)
    role = st.radio("", ["Admin", "Teacher", "Student"], horizontal=True, label_visibility="collapsed")
    
    # Form inputs
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        col1, col2 = st.columns([1, 2])
        with col1:
            remember_me = st.checkbox("Remember me")
        with col2:
            st.markdown('<div style="text-align: right;"><a href="#" class="auth-link">Forgot Password?</a></div>', unsafe_allow_html=True)
            
        submit = st.form_submit_button("Sign In")
        if submit:
            if not email or not password:
                st.error("Please fill in all fields!")
            else:
                st.success("Logged in successfully!")
                
    st.markdown("""
        <p class="auth-footer">
            Don't have an account? <a href="?page=signup" class="auth-link">Sign up here</a>
        </p>
    """, unsafe_allow_html=True) 