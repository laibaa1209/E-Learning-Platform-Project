import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def courses_page():
    st.markdown("""
        <div class="header-section">
            <h1 class="e-learning-title">Available Courses</h1>
            <p class="search-title">Explore our wide range of courses designed to help you succeed</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Course categories
    categories = ["All", "Programming", "Design", "Business", "Marketing"]
    selected_category = st.radio("", categories, horizontal=True, label_visibility="collapsed")
    
    # Sample courses data
    courses = [
        {
            "title": "Introduction to Python",
            "description": "Learn the basics of Python programming language",
            "duration": "8 weeks",
            "level": "Beginner",
            "rating": 4.5
        },
        {
            "title": "Web Development Bootcamp",
            "description": "Master HTML, CSS, and JavaScript",
            "duration": "12 weeks",
            "level": "Intermediate",
            "rating": 4.8
        },
        {
            "title": "Data Science Fundamentals",
            "description": "Learn data analysis and visualization",
            "duration": "10 weeks",
            "level": "Advanced",
            "rating": 4.7
        }
    ]
    
    # Display courses in a grid
    col1, col2 = st.columns(2)
    for i, course in enumerate(courses):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="course-card">
                <div class="course-badge">{course['level']}</div>
                <div class="course-content">
                    <h2 class="course-title">{course['title']}</h2>
                    <p class="course-description">{course['description']}</p>
                    <div class="course-meta">
                        <span>⏱️ {course['duration']}</span>
                        <span>⭐ {course['rating']}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Enroll Now", key=f"enroll_{i}"):
                st.success(f"Successfully enrolled in {course['title']}!") 