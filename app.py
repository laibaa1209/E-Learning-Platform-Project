import streamlit as st
import base64

# Page config
st.set_page_config(
    page_title="Beat The Deadline",
    layout="wide",
    page_icon="⏰",
    initial_sidebar_state="expanded"
)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def switch_page(page_name):
    st.session_state.page = page_name
    st.experimental_rerun()

# handle the logo properly
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Try to load the logo
try:
    logo_base64 = get_base64_of_bin_file('logo.png')
    logo_html = f'<img src="data:image/png;base64,{logo_base64}" class="sidebar-logo">'
except:
    # Fallback to a placeholder gradient if logo fails to load
    logo_html = '''
    <div class="logo-placeholder">
        <span>BTD</span>
    </div>
    '''

# Complete CSS 
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap');

    /* Enhanced Pattern Background */
    .stApp {
        background: 
            linear-gradient(135deg, rgba(35,58,125,0.15) 25%, transparent 25%) -10px 0,
            linear-gradient(225deg, rgba(35,58,125,0.15) 25%, transparent 25%) -10px 0,
            linear-gradient(315deg, rgba(35,58,125,0.15) 25%, transparent 25%),
            linear-gradient(45deg, rgba(35,58,125,0.15) 25%, transparent 25%);
        background-size: 30px 30px;  /* Made pattern larger */
        background-color: #1a1a1a !important;
    }

    /* Adjusted Background Overlay */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(26,26,26,0.92) 0%, rgba(13,17,23,0.90) 100%);
        pointer-events: none;
        z-index: 0;
    }

    /* Sidebar Styles */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #233a7d 0%, #1a1a1a 100%);
        border-right: 1px solid rgba(255,255,255,0.1);
        z-index: 1;
    }
    .sidebar-header {
        background: rgba(255,255,255,0.05);
        padding: 1.5rem 1rem;
        border-radius: 0 0 2rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    .sidebar-logo, .logo-placeholder {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        margin: 0 auto 1rem auto;
        display: block;
        border: 2px solid #42a5f5;
        box-shadow: 0 0 15px #42a5f5;
    }
    .logo-placeholder {
        background: linear-gradient(45deg, #233a7d, #42a5f5);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        font-weight: 800;
        color: white;
    }
    .sidebar-title {
        text-align: center;
        font-size: 1.4rem;
        font-weight: 700;
        background: linear-gradient(90deg, #42a5f5, #64b5f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.5rem 0;
        letter-spacing: 1px;
    }
    .nav-btn {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 1rem !important;
        color: #fff !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        margin: 0.5rem 0 !important;
        padding: 0.75rem 1.5rem !important;
        position: relative !important;
        overflow: hidden !important;
    }
    .nav-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.2),
            transparent
        );
        transition: 0.5s;
    }
    .nav-btn:hover::before {
        left: 100%;
    }
    .nav-btn:hover {
        background: rgba(66,165,245,0.2) !important;
        box-shadow: 0 0 20px rgba(66,165,245,0.3) !important;
        transform: translateY(-2px);
    }

    /* Main Content Styles */
    .main {
        z-index: 1;
    }
    .hero-container {
        background: linear-gradient(135deg, rgba(35,58,125,0.1) 0%, rgba(66,165,245,0.1) 100%);
        border-radius: 2rem;
        padding: 3rem 2rem;
        margin: 1rem 0;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .hero-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, #42a5f5, transparent);
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #fff, #42a5f5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.5rem;
        line-height: 1.2;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: rgba(255,255,255,0.7);
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    .stat-container {
        display: flex;
        gap: 2rem;
        margin-top: 3rem;
    }
    .stat-box {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 1rem;
        padding: 1.5rem;
        flex: 1;
        text-align: center;
        transition: transform 0.3s ease;
    }
    .stat-box:hover {
        transform: translateY(-5px);
        background: rgba(66,165,245,0.1);
    }
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        color: #42a5f5;
        margin-bottom: 0.5rem;
    }
    .stat-label {
        color: rgba(255,255,255,0.7);
        font-size: 0.9rem;
    }

    /* Enhanced Pattern Overlay */
    .stApp::after {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            repeating-linear-gradient(45deg, 
                rgba(66,165,245,0.08) 0px, 
                rgba(66,165,245,0.08) 1px,
                transparent 1px, 
                transparent 15px
            ),
            repeating-linear-gradient(-45deg, 
                rgba(35,58,125,0.08) 0px, 
                rgba(35,58,125,0.08) 1px,
                transparent 1px, 
                transparent 15px
            );
        pointer-events: none;
        z-index: 0;
    }

    /* Header Section Styles */
    .header-section {
        background: linear-gradient(135deg, rgba(35,58,125,0.1) 0%, rgba(66,165,245,0.1) 100%);
        border-radius: 2rem;
        padding: 2.5rem 2rem;
        margin: 1rem 0;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 4px 24px rgba(66,165,245,0.1);
        position: relative;
        overflow: hidden;
        animation: glow 3s ease-in-out infinite;
    }

    @keyframes glow {
        0% { box-shadow: 0 4px 24px rgba(66,165,245,0.1); }
        50% { box-shadow: 0 4px 34px rgba(66,165,245,0.3); }
        100% { box-shadow: 0 4px 24px rgba(66,165,245,0.1); }
    }

    .header-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.2),
            transparent
        );
        animation: shine 3s infinite;
    }

    @keyframes shine {
        0% { left: -100%; }
        50% { left: 100%; }
        100% { left: 100%; }
    }

    .search-content {
        flex: 1;
        padding-right: 3rem;
    }
    .e-learning-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #fff, #42a5f5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        animation: titleGlow 3s ease-in-out infinite;
    }

    @keyframes titleGlow {
        0% { text-shadow: 0 0 10px rgba(66,165,245,0.3); }
        50% { text-shadow: 0 0 20px rgba(66,165,245,0.5); }
        100% { text-shadow: 0 0 10px rgba(66,165,245,0.3); }
    }
    .search-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.8rem;
        font-weight: 600;
        color: rgba(255,255,255,0.7);
        margin-bottom: 1.5rem;
        line-height: 1.2;
    }
    .search-container {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 50px;
        padding: 0.8rem 1.5rem;
        display: flex;
        align-items: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        max-width: 450px;
        transition: all 0.3s ease;
    }
    .search-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(66,165,245,0.2);
        border-color: rgba(66,165,245,0.3);
    }
    .search-input {
        border: none;
        outline: none;
        width: 100%;
        font-family: 'Poppins', sans-serif;
        font-size: 1rem;
        color: #fff;
        background: transparent;
        padding: 0.5rem 0;
    }
    .search-input::placeholder {
        color: rgba(255,255,255,0.5);
    }
    .search-button {
        background: #42a5f5;
        color: white;
        border: none;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(66,165,245,0.3);
    }
    .search-button:hover {
        background: #1976d2;
        transform: scale(1.05);
    }
    .illustration-container {
        flex: 1;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .floating-illustration {
        max-width: 400px;
        animation: float 3s ease-in-out infinite;
        filter: drop-shadow(0 10px 20px rgba(66,165,245,0.2));
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }

    /* Fun Animated Top Bar */
    .fun-top-bar {
        position: fixed;
        top: 0;
        right: 0;
        left: 0;
        height: 70px;
        background: linear-gradient(90deg, #233a7d, #42a5f5);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 2rem;
        z-index: 1000;
        overflow: hidden;
    }
    
    /* Floating Bubbles Animation */
    .bubble {
        position: absolute;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
        animation: float-bubble 8s infinite;
        pointer-events: none;
    }
    .bubble:nth-child(1) { width: 60px; height: 60px; left: 10%; animation-delay: 0s; }
    .bubble:nth-child(2) { width: 40px; height: 40px; left: 30%; animation-delay: 2s; }
    .bubble:nth-child(3) { width: 50px; height: 50px; left: 50%; animation-delay: 4s; }
    .bubble:nth-child(4) { width: 45px; height: 45px; left: 70%; animation-delay: 6s; }

    @keyframes float-bubble {
        0% { transform: translateY(70px); opacity: 0; }
        50% { transform: translateY(20px); opacity: 0.5; }
        100% { transform: translateY(70px); opacity: 0; }
    }

    /* Fun Navigation Menu */
    .fun-nav {
        display: flex;
        gap: 1rem;
        align-items: center;
    }
    
    .nav-item {
        position: relative;
        padding: 0.8rem 1.5rem;
        color: white;
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
        border-radius: 20px;
        background: rgba(255,255,255,0.1);
        overflow: hidden;
    }
    
    .nav-item:hover {
        transform: translateY(-3px);
        background: rgba(255,255,255,0.2);
    }
    
    .nav-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.3),
            transparent
        );
        transition: 0.5s;
    }
    
    .nav-item:hover::before {
        left: 100%;
    }

    /* Enhanced Sidebar with Fun Elements */
    .sidebar-wrapper {
        background: linear-gradient(135deg, #233a7d 0%, #1a1a1a 100%);
        height: 100vh;
        padding: 2rem 1.5rem;
        position: relative;
    }

    .menu-item {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 16px;
        transition: all 0.3s ease;
        cursor: pointer;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
    }

    .menu-item:hover {
        background: rgba(66,165,245,0.15);
        transform: scale(1.02) translateX(5px);
    }

    .menu-icon {
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: rgba(66,165,245,0.1);
        font-size: 1.2rem;
    }

    .menu-text {
        color: white;
        font-weight: 500;
    }

    /* Fun Hover Cards for Stats */
    .stats-container {
        display: flex;
        gap: 1.5rem;
        margin-top: 2rem;
    }

    .stat-card {
        flex: 1;
        padding: 1.5rem;
        border-radius: 20px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }

    .stat-card:hover {
        transform: translateY(-5px) scale(1.02);
        background: rgba(66,165,245,0.1);
    }

    .stat-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        transform: translateX(-100%);
        transition: 0.5s;
    }

    .stat-card:hover::after {
        transform: translateX(100%);
    }

    /* Footer Section */
    .footer {
        background: linear-gradient(180deg, rgba(35,58,125,0.1) 0%, rgba(26,26,26,1) 100%);
        padding: 4rem 2rem 2rem 2rem;
        margin-top: 4rem;
        border-top: 1px solid rgba(255,255,255,0.1);
    }
    
    .footer-content {
        display: flex;
        flex-wrap: wrap;
        gap: 2rem;
        justify-content: space-between;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .footer-section {
        flex: 1;
        min-width: 250px;
    }
    
    .footer-title {
        color: #42a5f5;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        font-family: 'Poppins', sans-serif;
    }
    
    .team-member {
        margin-bottom: 1.5rem;
    }
    
    .member-name {
        color: white;
        font-size: 1.1rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .member-role {
        color: rgba(255,255,255,0.7);
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    
    .social-links {
        display: flex;
        gap: 1rem;
    }
    
    .social-link {
        color: rgba(255,255,255,0.7);
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    .social-link:hover {
        color: #42a5f5;
        transform: translateY(-2px);
    }
    
    .contact-item {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        color: rgba(255,255,255,0.7);
        margin-bottom: 1rem;
    }
    
    .contact-icon {
        color: #42a5f5;
        font-size: 1.2rem;
    }
    
    .quick-links {
        display: flex;
        flex-direction: column;
        gap: 0.8rem;
    }
    
    .quick-link {
        color: rgba(255,255,255,0.7);
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    .quick-link:hover {
        color: #42a5f5;
        transform: translateX(5px);
    }
    
    .copyright {
        text-align: center;
        color: rgba(255,255,255,0.5);
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid rgba(255,255,255,0.1);
    }

    .team-section {
        padding: 3rem 2rem;
        background: rgba(35,58,125,0.1);
        border-radius: 10px;
        margin: 2rem 0;
    }

    .section-title {
        color: #42a5f5;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 3rem;
        font-family: 'Poppins', sans-serif;
    }

    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }

    .team-member {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .team-member:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(66, 165, 245, 0.2);
    }

    .member-name {
        color: white;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .member-role {
        color: rgba(255,255,255,0.7);
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }

    .social-links {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
    }

    .social-link {
        color: #42a5f5;
        text-decoration: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        transition: all 0.3s ease;
        background: rgba(66, 165, 245, 0.1);
    }

    .social-link:hover {
        color: white;
        background: #42a5f5;
        transform: translateY(-2px);
    }

    .team-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: center;
        padding: 20px;
    }
    .team-member {
        padding: 20px;
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        width: 300px;
        text-align: center;
    }
    .member-name {
        color: white;
        font-size: 18px;
        margin-bottom: 10px;
    }
    .member-role {
        color: #42a5f5;
        margin-bottom: 15px;
    }
    .social-links {
        display: flex;
        justify-content: center;
        gap: 10px;
    }
    .social-link {
        color: #42a5f5;
        text-decoration: none;
        padding: 5px 10px;
        border-radius: 5px;
        background: rgba(66, 165, 245, 0.1);
    }
    .social-link:hover {
        background: #42a5f5;
        color: white;
    }

    .team-title {
        font-size: 2.5rem;
        color: white;
        text-align: center;
        margin-bottom: 3rem;
    }

    .team-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
        max-width: 300px;
        margin-left: auto;
        margin-right: auto;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        animation: cardGlow 3s ease-in-out infinite;
    }

    @keyframes cardGlow {
        0% { box-shadow: 0 4px 15px rgba(66,165,245,0.1); }
        50% { box-shadow: 0 4px 25px rgba(66,165,245,0.3); }
        100% { box-shadow: 0 4px 15px rgba(66,165,245,0.1); }
    }

    .team-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.2),
            transparent
        );
        animation: cardShine 3s infinite;
    }

    @keyframes cardShine {
        0% { left: -100%; }
        50% { left: 100%; }
        100% { left: 100%; }
    }

    .member-name {
        color: white;
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
        animation: nameGlow 3s ease-in-out infinite;
    }

    @keyframes nameGlow {
        0% { text-shadow: 0 0 10px rgba(255,255,255,0.3); }
        50% { text-shadow: 0 0 20px rgba(255,255,255,0.5); }
        100% { text-shadow: 0 0 10px rgba(255,255,255,0.3); }
    }

    .member-role {
        color: #42a5f5;
        font-size: 1.1rem;
        margin-bottom: 1rem;
        animation: roleGlow 3s ease-in-out infinite;
    }

    @keyframes roleGlow {
        0% { text-shadow: 0 0 10px rgba(66,165,245,0.3); }
        50% { text-shadow: 0 0 20px rgba(66,165,245,0.5); }
        100% { text-shadow: 0 0 10px rgba(66,165,245,0.3); }
    }

    .member-links {
        display: flex;
        justify-content: center;
        gap: 1rem;
    }

    .member-link {
        color: #42a5f5;
        text-decoration: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        background: rgba(66, 165, 245, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .member-link:hover {
        background: #42a5f5;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(66,165,245,0.3);
    }

    .member-link::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.3),
            transparent
        );
        transition: 0.5s;
    }

    .member-link:hover::before {
        left: 100%;
    }

    /* Login and Signup Page Styles */
    .auth-container {
        max-width: 1200px;
        margin: 2rem auto;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(66, 165, 245, 0.1);
    }

    .auth-title {
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #fff, #42a5f5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }

    .role-selection {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 2rem;
        margin-bottom: 3rem;
    }

    .role-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 1.5rem;
        padding: 2rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .role-card:hover {
        transform: translateY(-5px);
        background: rgba(66, 165, 245, 0.1);
        border-color: rgba(66, 165, 245, 0.3);
    }

    .role-card.selected {
        background: rgba(66, 165, 245, 0.15);
        border-color: #42a5f5;
        box-shadow: 0 0 20px rgba(66, 165, 245, 0.2);
    }

    .role-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        color: #42a5f5;
    }

    .role-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: white;
        margin-bottom: 0.5rem;
    }

    .role-description {
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.9rem;
        line-height: 1.5;
    }

    .auth-form {
        max-width: 500px;
        margin: 0 auto;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .form-group {
        margin-bottom: 1.5rem;
    }

    .form-label {
        display: block;
        color: white;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }

    .form-input {
        width: 100%;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 0.8rem;
        color: white;
        font-size: 1rem;
        transition: all 0.3s ease;
    }

    .form-input:focus {
        outline: none;
        border-color: #42a5f5;
        box-shadow: 0 0 10px rgba(66, 165, 245, 0.2);
    }

    .form-button {
        width: 100%;
        padding: 1rem;
        background: #42a5f5;
        color: white;
        border: none;
        border-radius: 0.8rem;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .form-button:hover {
        background: #1976d2;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(66, 165, 245, 0.3);
    }

    .auth-footer {
        text-align: center;
        margin-top: 2rem;
        color: rgba(255, 255, 255, 0.7);
    }

    .auth-link {
        color: #42a5f5;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
    }

    .auth-link:hover {
        color: #64b5f6;
        text-decoration: underline;
    }

    .stButton > button {
        width: 100%;
        padding: 0.75rem 1.5rem;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        color: white;
    }

    /* Button glow effect */
    .stButton > button {
        background-color: rgba(66, 165, 245, 0.1) !important;
        color: #fff !important;
        border: 1px solid rgba(66, 165, 245, 0.2) !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        background-color: rgba(66, 165, 245, 0.2) !important;
        box-shadow: 0 0 15px rgba(66, 165, 245, 0.5) !important;
        transform: translateY(-2px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
    if st.button("📚 Courses"):
        st.session_state.page = 'courses'
    if st.button("📝 Sign Up"):
        st.session_state.page = 'signup'
    if st.button("🔐 Login"):
        st.session_state.page = 'login'

# header section HTML
st.markdown(
    """
    <div class="header-section">
        <div class="search-content">
            <h1 class="e-learning-title">E-Learning</h1>
            <h2 class="search-title">Beat the Clock, Master the Skill</h2>
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


# Add the top bar
st.markdown(
    """
    <div class="fun-top-bar">
    </div>
    """,
    unsafe_allow_html=True
)

# First add the CSS
st.markdown("""
<style>
.team-title {
    font-size: 2.5rem;
    color: white;
    text-align: center;
    margin-bottom: 3rem;
}

.team-card {
    background: rgba(255, 255, 255, 0.05);
    padding: 2rem;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 2rem;
    max-width: 300px;
    margin-left: auto;
    margin-right: auto;
}

.member-name {
    color: white;
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}

.member-role {
    color: #42a5f5;
    font-size: 1.1rem;
    margin-bottom: 1rem;
}

.member-links {
    display: flex;
    justify-content: center;
    gap: 1rem;
}

.member-link {
    color: #42a5f5;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    background: rgba(66, 165, 245, 0.1);
}

.member-link:hover {
    background: #42a5f5;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='team-title'>Our Team</h1>", unsafe_allow_html=True)

# Team Member 1
st.markdown("""
<div class='team-card'>
    <div class='member-name'>Laiba Bint-e-Zia</div>
    <div class='member-role'>Full Stack Developer</div>
    <div class='member-links'>
        <a href='https://www.linkedin.com/in/laiba-zia-39899b286/' class='member-link' target='_blank'>LinkedIn</a>
        <a href='mailto:laibazia1209@gmail.com' class='member-link'>Email</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Team Member 2
st.markdown("""
<div class='team-card'>
    <div class='member-name'>Amna</div>
    <div class='member-role'>Full Stack Developer</div>
    <div class='member-links'>
        <a href='https://www.linkedin.com/in/amna-sakhi-b19723288/' class='member-link' target='_blank'>LinkedIn</a>
        <a href='mailto:amnasakhi2004@gmail.com' class='member-link'>Email</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Team Member 3
st.markdown("""
<div class='team-card'>
    <div class='member-name'>Hafsa Rashid</div>
    <div class='member-role'>Full Stack Developer</div>
    <div class='member-links'>
        <a href='https://www.linkedin.com/in/hafsa-rashid-08b6742b9/' class='member-link' target='_blank'>LinkedIn</a>
        <a href='mailto:laibazia6@gmail.com' class='member-link'>Email</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Login Page
if st.session_state.page == 'login':
    st.markdown("<h1 class='auth-title'>Welcome Back!</h1>", unsafe_allow_html=True)
    
    # Role selection at the top
    role = st.radio("Select your role:", ["Admin", "Teacher", "Student"], horizontal=True)
    
    # Login form
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            if email and password:
                st.success(f"Logged in successfully as {role}!")
                st.session_state.page = 'home'
            else:
                st.error("Please fill in all fields!")

# Signup Page
if st.session_state.page == 'signup':
    st.markdown("<h1 class='auth-title'>Create Account</h1>", unsafe_allow_html=True)
    
    # Role selection at the top (excluding Admin for signup)
    role = st.radio("Select your role:", ["Teacher", "Student"], horizontal=True)
    
    # Signup form
    with st.form("signup_form"):
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First Name")
        with col2:
            last_name = st.text_input("Last Name")
        
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        submit = st.form_submit_button("Sign Up")
        
        if submit:
            if not all([first_name, last_name, email, password, confirm_password]):
                st.error("Please fill in all fields!")
            elif password != confirm_password:
                st.error("Passwords don't match!")
            else:
                st.success(f"Account created successfully as {role}!")
                st.session_state.page = 'login'

# JavaScript for role selection and page switching
st.markdown("""
<script>
function selectRole(role) {
    document.querySelectorAll('.role-card').forEach(card => {
        card.classList.remove('selected');
    });
    event.currentTarget.classList.add('selected');
}

function switchPage(page) {
    // This will be handled by Streamlit's session state
    window.location.href = `?page=${page}`;
}
</script>
""", unsafe_allow_html=True)



