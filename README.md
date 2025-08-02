# ✍️ Essay Evaluation & Versioning API

This Django REST API simulates the backend for an AI-powered college admissions essay platform.  
It allows students to submit essays, upload multiple versions (PDF or DOCX), and auto-generates scorecards.

---

## 🚀 Features

- Create essays with student ID, college name, and question
- Upload essay versions (`.pdf` or `.docx`) as file uploads
- Auto-generate dummy scorecards for each version
- View all versions and the latest version with timestamps
- Django REST Framework based, easy to extend

---

## 🔧 Tech Stack

- Django 4.2+
- Django REST Framework
- SQLite (default DB)
- Python 3.8+

---

## 📁 Project Structure
essay_platform/
├── essay_platform/ 
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── essays/ 
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── ...
├── media/ # Uploaded files (auto-created)
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md




