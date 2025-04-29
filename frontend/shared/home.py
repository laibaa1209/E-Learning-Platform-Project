import streamlit as st
import base64
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def home_page():
    # Header section
    st.markdown(
        """
        <div class="header-section">
            <div class="search-content">
                <div class="e-learning-title">E-Learning</div>
                <div class="platform-text">Platform</div>
                <div class="search-title">Beat the Clock, Master the Skill</div>
                <div class="search-container">
                    <input type="text" class="search-input" placeholder="Search for courses...">
                    <button class="search-button">🔍</button>
                </div>
            </div>
            <div class="illustration-container">
                <img src="https://cdn-icons-png.flaticon.com/512/2641/2641333.png" 
                     class="floating-illustration" 
                     alt="Online Learning">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Main content
    st.markdown(
        """
        <div class="hero-container">
            <div class="hero-title">
                Transform Your Learning Journey
            </div>
            <div class="hero-subtitle">
                Join thousands of students who are mastering new skills and beating deadlines with our innovative learning platform.
            </div>
            <div class="stat-container">
                <div class="stat-box">
                    <div class="stat-number">15K+</div>
                    <div class="stat-label">Active Students</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number">500+</div>
                    <div class="stat-label">Expert Courses</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number">98%</div>
                    <div class="stat-label">Success Rate</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Team section
    st.markdown("<h1 class='team-title'>Our Team</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class='team-card'>
            <div class='member-name'>Laiba Bint-e-Zia</div>
            <div class='member-role'>Full Stack Developer</div>
            <div class='member-links'>
                <a href='{os.getenv('LAIBA_LINKEDIN', '#')}' class='member-link' target='_blank'>LinkedIn</a>
                <a href='mailto:{os.getenv('LAIBA_EMAIL', '')}' class='member-link'>Email</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='team-card'>
            <div class='member-name'>Amna</div>
            <div class='member-role'>Full Stack Developer</div>
            <div class='member-links'>
                <a href='{os.getenv('AMNA_LINKEDIN', '#')}' class='member-link' target='_blank'>LinkedIn</a>
                <a href='mailto:{os.getenv('AMNA_EMAIL', '')}' class='member-link'>Email</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='team-card'>
            <div class='member-name'>Hafsa Rashid</div>
            <div class='member-role'>Full Stack Developer</div>
            <div class='member-links'>
                <a href='{os.getenv('HAFSA_LINKEDIN', '#')}' class='member-link' target='_blank'>LinkedIn</a>
                <a href='mailto:{os.getenv('HAFSA_EMAIL', '')}' class='member-link'>Email</a>
            </div>
        </div>
        """, unsafe_allow_html=True) 