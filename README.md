# 📰 News App API

A backend REST API for managing news articles using **FastAPI** and **MySQL**.

This project supports:
- Creating news
- Viewing all news
- Updating news
- Deleting news

---

## 🚀 Tech Stack

- **Backend Framework:** FastAPI
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Server:** Uvicorn
- **Language:** Python 3.11

---

## 📂 Project Structure
news_app/ ├── backend/ │   ├── app/ │   │   ├── main.py │   │   ├── routes.py │   │   ├── models.py │   │   ├── schemas.py │   │   └── database.py │   ├── venv/ │   └── .env └── README.md
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone / Open Project
```bash
cd news_app
2️⃣ Activate Virtual Environment
Bash
Copy code
cd backend
source venv/bin/activate
3️⃣ Install Dependencies
Bash
Copy code
pip install fastapi uvicorn sqlalchemy pymysql python-dotenv
🗄️ Database Configuration
Create MySQL database:
Sql
Copy code
CREATE DATABASE news_db;
Update .env file:
Env
Copy code
DB_USER=root
DB_PASS=your_mysql_password
DB_HOST=localhost
DB_NAME=news_db
▶️ Run the Server
Bash
Copy code
uvicorn app.main:app --reload
Server will run at:
Copy code

http://127.0.0.1:8000
Swagger UI:
Copy code

http://127.0.0.1:8000/docs
📌 API Endpoints
🔹 Create News
POST /news
Json
Copy code
{
  "title": "Breaking News",
  "content": "This is news content",
  "category": "Politics"
}
🔹 Get All News
GET /news
🔹 Update News
PUT /news/{news_id}
Json
Copy code
{
  "title": "Updated Title",
  "content": "Updated Content",
  "category": "Tech"
}
🔹 Delete News
DELETE /news/{news_id}
✅ Status
✔ CRUD APIs working
✔ Database connected
✔ Swagger UI enabled
📌 Future Enhancements
Authentication (Admin / Editor)
Pagination
Search & Filter
Deployment on Railway / Render
👨‍💻 Developer
Suraj Pawar
FY B.Sc Computer Science
FastAPI | MySQL | Backend Developer