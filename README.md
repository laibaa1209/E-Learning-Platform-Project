# E-Learning Platform

A modern e-learning platform built with Streamlit, designed to help students and teachers manage their learning journey effectively.

## Project Structure

```
OLP-Website/
├── frontend/
│   ├── admin/           # Admin-specific frontend components
│   ├── teacher/         # Teacher-specific frontend components
│   ├── student/         # Student-specific frontend components
│   └── shared/          # Shared frontend components
│       ├── home.py      # Home page
│       ├── login.py     # Login page
│       ├── signup.py    # Signup page
│       ├── courses.py   # Courses page
│       └── styles.css   # Shared styles
├── backend/
│   ├── api/            # API endpoints
│   ├── models/         # Database models
│   ├── services/       # Business logic
│   └── utils/          # Utility functions
├── assets/
│   ├── images/         # Image assets
│   ├── videos/         # Video lectures
│   └── icons/          # Icon assets
├── docs/               # Documentation
├── app.py             # Main application file
├── requirements.txt   # Python dependencies
└── .env              # Environment variables (not tracked in git)
```

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd OLP-Website
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following variables:
```
LAIBA_LINKEDIN="your_linkedin_url"
LAIBA_EMAIL="your_email"

AMNA_LINKEDIN="your_linkedin_url"
AMNA_EMAIL="your_email"

HAFSA_LINKEDIN="your_linkedin_url"
HAFSA_EMAIL="your_email"
```

5. Run the application:
```bash
streamlit run app.py
```

## Features

- User authentication (Admin, Teacher, Student roles)
- Course browsing and enrollment
- Interactive learning materials
- Progress tracking
- Responsive design

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
