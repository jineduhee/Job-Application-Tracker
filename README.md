# Job-Application-Tracker
A simple job application tracker that utilises python, html, api's, sound and etc.

NOTE: I've created this full-stack application that covers front-end and back-end, however, I am unable publish this full-stack version on GitHub Pages hence why I'll have the static implementation available on here alongside the full-stack implementation.

## Live Demo (No installation needed)

**Static Version (GitHub Pages):** [https://jineduhee.github.io/Job-Application-Tracker](https://jineduhee.github.io/Job-Application-Tracker)

## Features

- **Full-stack application** with FastAPI backend and SQLite database
- **Modern UI** with smooth animations and sound effects
- **CRUD operations** - Create, Read, Update, Delete job applications
- **AI-powered job extraction** from URLs (requires OpenAI API key)
- **Responsive design** - works on mobile and desktop
- **Real-time notifications** with sound and vibration feedback
- **Status tracking** with predefined dropdown options
- **Notes system** for additional application details

## TechStack

**Backend:**
- FastAPI - Modern Python web framework
- SQLAlchemy - Simple Database ORM
- SQLite - Lightweight database
- Pydantic - Simple Data validation

**Frontend:**
- HTML5, CSS3, JavaScript (Vanilla)
- Responsive design with Flexbox
- CSS animations and transitions
- Web Audio API for sound effects

## Quick Start

### Prerequisites
- Python 3.8+ installed
- Git installed
- IDE

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jineduhee/Job-Application-Tracker.git
   cd Job-Application-Tracker
   ```

2. **Set Up Python Virtual Environment**
   ```bash
   # Create virtual environment
   python3 -m venv venv

   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   # Start the FastAPI server
   uvicorn app.main:app --reload
   ```

5. **Access the Application**
   Open your browser and go to:
   ```
   http://127.0.0.1:8000
   ```

## Project Structure

```
Job-Application-Tracker/
├── app/                    # Backend (FastAPI)
│   ├── main.py            # API routes and server
│   ├── models.py          # Database models
│   ├── crud.py            # Database operations
│   ├── database.py        # Database connection
│   └── job_extractor.py   # AI job extraction
├── static/                # Frontend files
│   ├── index.html         # Main page
│   ├── style.css          # Styling
│   └── ding.mp3           # Notification sound
├── index.html             # Static version (GitHub Pages)
├── style.css              # Static version CSS
├── ding.mp3               # Static version sound
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```