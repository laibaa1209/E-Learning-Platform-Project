import streamlit as st

def create_header():
    st.markdown("""
        <div class="header-section">
            <div class="search-content">
                <h1 class="e-learning-title">Online Learning Platform</h1>
            </div>
        </div>
    """, unsafe_allow_html=True)

def create_footer():
    st.markdown("""
        <div class="footer">
            <p>© 2024 Online Learning Platform. All rights reserved.</p>
        </div>
    """, unsafe_allow_html=True) 