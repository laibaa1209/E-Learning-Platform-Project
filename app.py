import streamlit as st
import sys
from pathlib import Path

# Add the frontend directory to the Python path
frontend_dir = Path(__file__).parent / 'frontend'
sys.path.append(str(frontend_dir))

from frontend.shared.home import home_page
from frontend.shared.login import login_page
from frontend.shared.signup import signup_page
from frontend.shared.courses import courses_page
import base64
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure the page
st.set_page_config(
    page_title="Beat The Deadline - E-Learning Platform",
    page_icon="📚",
    layout="wide"
)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# handle the logo properly
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Try to load the logo
try:
    logo_base64 = get_base64_of_bin_file('assets/images/logo.png')
    logo_html = f'<img src="data:image/png;base64,{logo_base64}" class="sidebar-logo">'
except:
    # Fallback to a placeholder gradient if logo fails to load
    logo_html = '''
    <div class="logo-placeholder">
        <span>BTD</span>
    </div>
    '''

# Load CSS from shared styles
with open('frontend/shared/styles.css', 'r') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.markdown(
        f"""
        <div class="sidebar-header">
            {logo_html}
            <div class="sidebar-title">Beat The Deadline</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Navigation buttons
    if st.button("🏚️ Home"):
        st.session_state.page = 'home'
        st.rerun()
    if st.button("📚 Courses"):
        st.session_state.page = 'courses'
        st.rerun()
    if st.button("📝 Sign Up"):
        st.session_state.page = 'signup'
        st.rerun()
    if st.button("🔐 Login"):
        st.session_state.page = 'login'
        st.rerun()

# Page routing
if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'login':
    login_page()
elif st.session_state.page == 'signup':
    signup_page()
elif st.session_state.page == 'courses':
    courses_page()



