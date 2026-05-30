# 🚀 Lead Management Backend (FastAPI + MySQL)

A backend application built using FastAPI and MySQL for managing real estate leads. The project supports authentication, authorization, lead ownership, and full CRUD operations through REST APIs.

---

## 📌 Features

### Lead Management

✅ Create Lead

✅ Get All Leads

✅ Get Single Lead

✅ Update Lead

✅ Delete Lead

### Authentication & Authorization

✅ User Signup

✅ User Login

✅ Password Hashing using bcrypt

✅ JWT Authentication

✅ Protected Routes

✅ User-specific Lead Ownership

✅ Authorization (Users can access only their own leads)

### Backend Architecture

✅ Service Layer Architecture

✅ Dependency Injection

✅ Pydantic Request Validation

✅ Environment Variables (.env)

---

## 🧠 Tech Stack

**Backend Framework:** FastAPI

**Database:** MySQL

**Language:** Python

**Authentication:** JWT + OAuth2PasswordBearer

**Password Security:** bcrypt (Passlib)

**API Testing:** Swagger UI

**Configuration:** python-dotenv

---

## 📂 Project Structure

```text
fastapi/
│
├── routes/
│   ├── auth.py
│   └── leads.py
│
├── services/
│   ├── auth_service.py
│   └── lead_service.py
│
├── schemas.py
├── db.py
├── main.py
├── .env
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/kratitechie/lead-management-backend.git
cd lead-management-backend
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create MySQL Database

```sql
CREATE DATABASE fast_api_project;
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=fast_api_project

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run Server

```bash
python -m uvicorn main:app --reload
```

### 6. Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## 🔄 API Endpoints

### Authentication

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| POST   | /signup  | Create User |
| POST   | /login   | Login User  |

### Leads

| Method | Endpoint    | Description     |
| ------ | ----------- | --------------- |
| POST   | /lead       | Create Lead     |
| GET    | /leads      | Get User Leads  |
| GET    | /leads/{id} | Get Single Lead |
| PATCH  | /leads/{id} | Update Lead     |
| DELETE | /leads/{id} | Delete Lead     |

---

## 🧠 Key Concepts Implemented

* REST API Design
* FastAPI Dependency Injection
* Service Layer Architecture
* JWT Authentication
* Authorization & Ownership
* Password Hashing (bcrypt)
* Environment Variables
* Dynamic SQL Query Building
* MySQL Integration
* Pydantic Validation
* Error Handling

---

## 🚀 Future Improvements

* Deployment (Render/Railway)
* Pagination
* Sorting & Search
* Refresh Tokens
* Docker Support
* Role-Based Access Control (RBAC)

---

## 👩‍💻 Author

Krati Bhatia

---

⭐ If you found this useful, consider giving it a star!
