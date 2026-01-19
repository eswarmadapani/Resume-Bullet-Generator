# Resume Bullet Generator - Backend

Backend API for the Resume Bullet Generator application.

## Setup

1. Create virtual environment: `python -m venv venv`
2. Activate virtual environment: `.\venv\Scripts\Activate.ps1`
3. Install dependencies: `pip install -r requirements.txt`
4. Download spaCy model: `python -m spacy download en_core_web_sm`
5. Run server: `uvicorn app.main:app --reload`
