# Online Course Django App — Assessment Feature

A starter Django project demonstrating course lessons, multiple-choice questions, choices, student submissions, and exam-result evaluation.

## Setup

```bash
python -m venv venv
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and `http://127.0.0.1:8000/admin/`.

## Important
This is a runnable starter implementation, not a copy of your course lab's exact code or screenshots. Review it, test it locally, and adapt it to the course requirements before submitting. The admin screenshot and successful mock-exam screenshot must be captured from your own running app.
