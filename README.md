# 🚀 Lead Management Backend (FastAPI + MySQL)

A backend system built using FastAPI and MySQL to manage real estate leads with full CRUD functionality.

---

## 📌 Features

* ✅ Create Lead (POST /leads)
* ✅ Get All Leads (GET /leads with filters)
* ✅ Get Single Lead (GET /leads/{id})
* ✅ Update Lead (PATCH /leads/{id})
* ✅ Delete Lead (DELETE /leads/{id})

---

## 🧠 Tech Stack

* **Backend Framework:** FastAPI
* **Database:** MySQL
* **Language:** Python
* **API Testing:** Swagger UI (/docs)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/kratitechie/lead-management-backend.git
cd lead-management-backend
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Setup MySQL Database

Run the following queries in MySQL:

```sql
CREATE DATABASE fast_api_project;

USE fast_api_project;

CREATE TABLE leads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    requirement TEXT,
    budget VARCHAR(50),
    location VARCHAR(100),
    stage VARCHAR(50),
    loan_required BOOLEAN,
    status VARCHAR(50) DEFAULT 'new',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 4. Run the server

```bash
python -m uvicorn main:app --reload
```

---

### 5. Open API Docs

👉 http://127.0.0.1:8000/docs

---

## 🔄 API Endpoints Overview

| Method | Endpoint    | Description             |
| ------ | ----------- | ----------------------- |
| POST   | /leads      | Create a new lead       |
| GET    | /leads      | Get all leads (filters) |
| GET    | /leads/{id} | Get single lead by ID   |
| PATCH  | /leads/{id} | Update lead             |
| DELETE | /leads/{id} | Delete lead             |

---

## 🧠 Key Concepts Implemented

* RESTful API design
* Request validation using Pydantic
* Dynamic SQL queries (filters & updates)
* MySQL integration with Python
* Error handling

---

## ⚠️ Note

* Database credentials are currently hardcoded (for learning purposes).
* In production, use environment variables (.env).

---

## 🚀 Future Improvements

* Authentication (JWT-based login/signup)
* Project structure refactor (routes, db separation)
* Deployment (Render / Railway)
* Pagination & advanced filtering

---

## 👩‍💻 Author

**Krati Bhatia**

---

## ⭐ If you found this useful, consider giving it a star!
