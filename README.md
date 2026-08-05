# 🎉 Event Management System

A multi-role event management platform built with Django, designed to let Admins, Organizers, and Participants manage and engage with events through dedicated, role-based dashboards.

---

## 📖 Overview

Event Management System is a Django MVT-based web application that streamlines how events are created, organized, and attended. Instead of a single generic interface, the platform provides **separate, tailored dashboards** for three distinct user roles — making event coordination clear and conflict-free for everyone involved.

---

## ✨ Features

- **Multi-Role Dashboards** — Dedicated views and permissions for Admin, Organizer, and Participant roles
- **Secure Authentication** — Built on Django's native auth system with permission-based access control
- **CSRF Protection & Input Validation** — Every form and endpoint is protected against common web vulnerabilities
- **Relational Database Design** — A well-structured schema modeling events, roles, and participation
- **Optimized ORM Queries** — Queries tuned to eliminate N+1 issues, keeping the app fast as data grows

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django (MVT Architecture) |
| Database | Supabase |
| Frontend | TailwindCSS |
| Auth & Security | Django's built-in authentication, CSRF protection |

---

## 🧩 How It Works

1. **Admin** — Oversees the platform, manages users, and has full visibility into all events
2. **Organizer** — Creates and manages events, tracks participant registrations
3. **Participant** — Browses available events and registers to attend

Each role sees only what's relevant to them, reducing clutter and preventing unauthorized actions — enforced at the view level using Django's permission system.

---

## 🗄️ Database Design

The schema was designed relationally to cleanly represent the connections between users, roles, and events, with ORM queries optimized to avoid the classic **N+1 query problem** — ensuring dashboards load efficiently even as the number of events and participants scales up.

---

## 🚀 Getting Started (Local Setup)

\`\`\`bash
# Clone the repository
git clone https://github.com/tazul9770/SDT_event_management
cd SDT_event_management

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser (Admin access)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
\`\`\`

Visit \`http://127.0.0.1:8000/\` in your browser to see the app running locally.

---

## 👤 Author

**Tazul Islam**
Backend / Full Stack Developer (Django/React)

---

## 📄 License

This project is open for learning and reference purposes. Feel free to explore the code and reach out with any questions.