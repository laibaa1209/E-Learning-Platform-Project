import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import sys

# Add the frontend directory to the Python path
frontend_dir = Path(__file__).parent.parent
sys.path.append(str(frontend_dir))

from frontend.shared.styles import load_css

# Load custom CSS
load_css()

def login_page():
    # Initialize session state if not exists
    if 'selected_role' not in st.session_state:
        st.session_state.selected_role = None
    
    # Welcome container
    st.markdown("""
        <div class="auth-header-section">
            <div class="auth-search-content">
                <h1 class="auth-title">Welcome Back!</h1>
                <p class="auth-subtitle">Please select your role to continue</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Role selection cards
    if st.session_state.selected_role is None:
        st.markdown('<div class="role-cards-container">', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
                <div class="role-card">
                    <div class="role-icon">👨‍💼</div>
                    <h3 class="role-title">Admin</h3>
                    <p class="role-description">Access system administration and management features</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Continue as Admin", key="admin_card", type="primary"):
                st.session_state.selected_role = "admin"
                st.experimental_rerun()
        
        with col2:
            st.markdown("""
                <div class="role-card">
                    <div class="role-icon">👨‍🏫</div>
                    <h3 class="role-title">Teacher</h3>
                    <p class="role-description">Manage courses and interact with students</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Continue as Teacher", key="teacher_card", type="primary"):
                st.session_state.selected_role = "teacher"
                st.experimental_rerun()
        
        with col3:
            st.markdown("""
                <div class="role-card">
                    <div class="role-icon">👨‍🎓</div>
                    <h3 class="role-title">Student</h3>
                    <p class="role-description">Access courses and learning materials</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Continue as Student", key="student_card", type="primary"):
                st.session_state.selected_role = "student"
                st.experimental_rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Show login form for selected role
    if st.session_state.selected_role:
        st.markdown('<div class="auth-form">', unsafe_allow_html=True)
        create_login_form(st.session_state.selected_role)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Back button
        if st.button("← Back to Role Selection"):
            st.session_state.selected_role = None
            st.experimental_rerun()

def create_login_form(role):
    with st.form(f"login_form_{role}"):
        st.markdown(f'<h2 class="auth-form-title">{role.title()} Login</h2>', unsafe_allow_html=True)
        
        email = st.text_input("Email", key=f"email_{role}")
        password = st.text_input("Password", type="password", key=f"password_{role}")
        
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            st.success(f"Login successful as {role}!")
            st.switch_page("frontend/shared/courses.py")

if __name__ == "__main__":
    login_page() 
