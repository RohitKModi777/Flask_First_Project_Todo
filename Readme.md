# 📝 Flask Todo App

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-white?logo=flask)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0-green?logo=mongodb)](https://www.mongodb.com/)

A simple, modern **Todo web application** built using **Flask** and **MongoDB**.  
Manage tasks efficiently with user authentication and a clean, responsive interface.

---

## 🌟 Features

- **User Authentication**
  - Secure login and logout.
  - Manual registration: To create a new user, **visit `/register` manually** in your browser.
- **Task Management**
  - Add, delete, and track tasks.
  - Color-coded status badges: Pending, Working, Done.
- **Responsive & Modern UI**
  - Smooth hover effects, badges, and buttons.
- **Flash Messages**
  - Informative feedback for actions like login, logout, or task updates.

---

## ⚡ How It Works

1. **Authentication**
   - Log in with a registered user.
   - First-time users must manually type `/register` in the browser to create an account.

2. **Task Management**
   - Add tasks via the input form.
   - Track task status with badges.
   - Delete or clear tasks as needed.

3. **Database**
   - Uses **MongoDB** to store users and tasks.
   - Collections are created automatically when the first entry is added.

4. **Navigation**
   - Header with navigation links.
   - Footer with app credits.

---

## 🎨 UI Highlights

- **Header:** Gradient background with centered app name.
- **Login/Registration Box:** Rounded card with shadows and hover effects.
- **Task Cards:** Rounded, shadowed boxes for focus.
- **Buttons:** Colored buttons with hover animations.
- **Status Badges:**  
  - Pending → Yellow  
  - Working → Blue  
  - Done → Green  

---

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/yourusername/flask-todo-app.git
cd flask-todo-app
export SECRET_KEY="your-secret-key"
export MONGO_URI="your-mongo-uri"
python run.py
```
Open your browser: http://127.0.0.1:5000

Register manually: Type /register in the URL bar to create a new user.

Log in and start managing your tasks!

💡 Future Enhancements

Add a user-friendly registration form instead of manual URL access.

Task editing, filtering, and prioritization.

Dark mode toggle.

Deploy on platforms like Vercel or Heroku.

📌 Notes

Designed as a learning project for Flask beginners.

MongoDB collections are automatically created.

Focused on core Flask concepts: routing, templates, blueprints, and database integration.

🎯 Key Takeaways

Flask app structure with app factory and blueprints.

User authentication with Flask-Login.

Database integration with Flask-PyMongo.

Modern, responsive UI using CSS.

Interactive flash messages for feedback.
