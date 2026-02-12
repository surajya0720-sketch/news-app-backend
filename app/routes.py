from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
import bcrypt

router = APIRouter()

# ======================
# 🔐 ADMIN LOGIN
# ======================

@router.post("/admin/login")
def admin_login(username: str, password: str, db: Session = Depends(get_db)):
    admin = db.query(models.Admin).filter(models.Admin.username == username).first()

    if not admin:
        raise HTTPException(status_code=401, detail="Invalid username")

    if not bcrypt.checkpw(password.encode('utf-8'), admin.password_hash.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"message": "Login successful"}


# ======================
# 📰 GET ALL NEWS
# ======================

@router.get("/news/")
def get_news(db: Session = Depends(get_db)):
    news = db.query(models.News).all()
    return news