# 💸 Expense Tracker API

Track every coin. Stay on top of your finances with this secure, verified, and scalable RESTful API built with Django and Django REST Framework.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![OpenAPI](https://img.shields.io/badge/OpenAPI-3.0-blue)

---

## 🚀 Live Demo

🟢 **API Base URL**: https://nigeys-expense-tracker.onrender.com/api/v1/  
🔐 *Note: Email verification is required to log in.*

---

## 🧩 Features

- ✅ User registration & login via email
- ✅ **Mandatory email verification** (via django-allauth)
- ✅ JWT authentication using SimpleJWT & dj-rest-auth
- ✅ Create, read, update, and delete expenses
- ✅ Custom expense categories
- ✅ Filter by date, category, or amount
- ✅ Per-user data access — each user sees only their expenses
- ✅ Fully deployed with Render and Supabase PostgreSQL

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **admin dashboard**: [django-jazzmin](https://github.com/farridav/django-jazzmin)
- **Authentication**: SimpleJWT, dj-rest-auth, django-allauth
- **Database**: PostgreSQL (via [Supabase](https://supabase.com))
- **Deployment**: [Render](https://render.com)
- **Dev Tools**: Python `httpx`

---

## 🛡️ Authentication Flow

1. User registers with email
2. Verification email is sent
3. After verification, user can log in and access protected endpoints
4. JWT access/refresh tokens are returned

---

## 📦 Setup & Installation

### 🔧 Requirements

- Python 3.10+
- pip
- Git

### 🔄 Clone the repo

```bash
git clone https://github.com/chips35x7/Expense-Tracker-Version-1.0.git
cd expense-tracker

📦 Install dependencies
pip install -r requirements.txt

⚙️ Set environment variables
Create a .env file and add:
      SECRET_KEY=your_django_secret_key
      DEBUG=True
      DATABASE_URL=database-url
      EMAIL_HOST_PASSWORD = email_password
      EMAIL_HOST_USER = host
      DJANGO_SUPERUSER_USERNAME = your_username (OPTIONAL)
      DJANGO_SUPERUSER_EMAIL = your_email (OPTIONAL)
      DJANGO_SUPERUSER_PASSWORD = your_password (OPTIONAL)

🔨 Run migrations
python manage.py migrate

🔐 Example API Usage
🔑 Register
POST /auth/registration/

{
  "email": "user@example.com",
  "password1": "strongpass123",
  "password2": "strongpass123"
}

🔐 Login (after email verification)
POST /auth/login/

Returns:
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}

💰 Add Expense
POST https://nigeys-expense-tracker.onrender.com/api/v1/

{
  "title": "Groceries",
  "amount": 23.50,
  "category": "Food",
  "date": "2025-07-24"
}
Include your token in the Authorization header:
Bearer your_access_token

---

## 📚 API Documentation

This API follows the OpenAPI 3.0 specification, powered by `drf-spectacular`.
Use This As the Base URL -->  https://nigeys-expense-tracker.onrender.com

- 🔹 **Swagger UI**  
  👉 [`/api/schema/swagger-ui/`](https://your-api.onrender.com/api/schema/swagger/)

- 🔹 **Redoc UI**  
  👉 [`/api/schema/redoc/`](https://your-api.onrender.com/api/docs/redoc/)

- 🔹 **Dynamic OpenAPI Schema** (JSON)  
  👉 [`/api/schema/`](https://your-api.onrender.com/api/schema/)

- 🔹 **Static YAML Schema File**  
  👉 [`schema.yml`](./schema.yml) In project base directory

> The static schema is version-controlled for easier integration with external tools and frontend apps.


🧪 Testing
Use tools like Postman or httpx for testing.

🤝 License
This project is licensed under the MIT License.

✨ Acknowledgements
**Django REST Framework
**django-jazzmin
**dj-rest-auth
**SimpleJWT
**Supabase
**Render
