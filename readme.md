# 🔗 Link Shortener

A simple Django-based URL shortener that converts long and cumbersome URLs into short links.  
This was my **first Django project**, created to learn the basics of Django models, views, and routing.

> 🌐 **Live Demo**: [link.pythonanywhere.com](https://link.pythonanywhere.com/)

---

## ✨ Features

- Shortens any valid URL into an **8-character alphanumeric** link.
- Minimal and clean interface.
- Uses Django’s built-in capabilities for routing and database management.

---

## 🛠 Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (default)
- **Hosting**: PythonAnywhere

---

## 📦 Installation (Local Setup)

1. **Clone the repository**
   ```bash
   git clone https://github.com/Naman-0206/Link_Shortner.git
   cd Link_Shortner
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**

   ```bash
   python manage.py migrate
   ```

4. **Start the development server**

   ```bash
   python manage.py runserver
   ```

5. Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser.
