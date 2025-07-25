# 🎥 Anime Streaming Website

A basic anime streaming website built using **Django**, **PostgresSql**, **HTML**, **CSS**, and **JavaScript**.  
This app allows users to browse anime, view episode lists, and stream episodes (if integrated with a media player).

---

## 🚀 Features

- Home Page listing all anime
- Individual Anime Detail Page
- Episode listing per anime
- Django Admin Panel for content management
- MySQL Database integration
- Ready to deploy on [Railway](https://railway.app/)

---

## 🛠 Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- Database: MySQL (can also use SQLite for development)
- Hosting: Railway

---

## 🧩 Project Structure

anime-streaming/
│
├── anime_stream/ # Django Project
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── anime/ # Main App (Anime, Episodes)
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/anime/
│ ├── home.html
│ └── anime_detail.html
│
├── media/ # Media uploads
├── requirements.txt
├── manage.py
└── Procfile # For Railway deployment

yaml
Copy
Edit

---

## 🧪 Setup Instructions (Local)

### 1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/anime-streaming.git
   cd anime-streaming
### Create virtual environment


python -m venv env
source env/bin/activate   # On Windows use: env\Scripts\activate
### Install dependencies


pip install -r requirements.txt
### Apply migrations

python manage.py makemigrations
python manage.py migrate
### Run the server

python manage.py runserver
###  Railway Deployment
Create a Railway account

Connect your GitHub repo

Add required environment variables (SECRET_KEY, DEBUG, ALLOWED_HOSTS)

### Set build command:


pip install -r requirements.txt
### Set start command:


gunicorn anime_stream.wsgi
Done! Your app will be live 🚀

