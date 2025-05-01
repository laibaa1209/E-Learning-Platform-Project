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

def signup_page():
    # Initialize session state
    if 'selected_role' not in st.session_state:
        st.session_state['selected_role'] = None

    # Welcome container
    st.markdown("""
        <div class="auth-header-section">
            <div class="auth-search-content">
                <h1 class="auth-title">Welcome!</h1>
                <p class="auth-subtitle">Greeting's New User</p>
                <p class="auth-sub-headline">Please select your role to continue</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Role selection cards
    if st.session_state['selected_role'] is None:
        st.markdown('<div class="role-cards-container">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
                <div class="role-card">
                    <div class="role-icon">👨‍🏫</div>
                    <h3 class="role-title">Teacher</h3>
                    <p class="role-description">Join as an educator and share your knowledge</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Continue as Teacher", key="teacher_card", type="primary"):
                st.session_state['selected_role'] = "teacher"
                st.rerun()
        
        with col2:
            st.markdown("""
                <div class="role-card">
                    <div class="role-icon">👨‍🎓</div>
                    <h3 class="role-title">Student</h3>
                    <p class="role-description">Start your learning journey with us</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Continue as Student", key="student_card", type="primary"):
                st.session_state['selected_role'] = "student"
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Show signup form for selected role
    if st.session_state['selected_role']:
        st.markdown('<div class="auth-form">', unsafe_allow_html=True)
        create_signup_form(st.session_state['selected_role'])
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Back button
        if st.button("← Back to Role Selection"):
            st.session_state['selected_role'] = None
            st.rerun()

def create_signup_form(role):
    with st.form(f"signup_form_{role}"):
        st.markdown(f'<h2 class="auth-form-title">{role.title()} Signup</h2>', unsafe_allow_html=True)
        
        full_name = st.text_input("Full Name", key=f"name_{role}")
        email = st.text_input("Email", key=f"email_{role}")
        password = st.text_input("Password", type="password", key=f"password_{role}")
        confirm_password = st.text_input("Confirm Password", type="password", key=f"confirm_password_{role}")
        
        # Additional fields based on role
        if role == "teacher":
            department = st.text_input("Department", key=f"department_{role}")
            qualification = st.text_input("Qualification", key=f"qualification_{role}")
        elif role == "student":
            student_id = st.text_input("Student ID", key=f"student_id_{role}")
            semester = st.selectbox("Semester", range(1, 9), key=f"semester_{role}")
        
        submit_button = st.form_submit_button("Sign Up")
        
        if submit_button:
            # Here you would typically handle the signup logic
            st.success(f"Signup successful as {role}!")
            # Redirect to login page
            st.switch_page("frontend/shared/login.py")

if __name__ == "__main__":
    signup_page() 
