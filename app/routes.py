from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/news",
    tags=["News"]
)

# =========================
# CREATE NEWS
# =========================
@router.post("/", response_model=schemas.NewsResponse)
def create_news(news: schemas.NewsCreate, db: Session = Depends(get_db)):

    new_news = models.News(
        title=news.title,
        content=news.content,
        category=news.category
    )

    db.add(new_news)
    db.commit()
    db.refresh(new_news)

    return new_news


# =========================
# GET ALL NEWS
# =========================
@router.get("/", response_model=list[schemas.NewsResponse])
def get_news(db: Session = Depends(get_db)):

    news = db.query(models.News).all()
    return news


# =========================
# GET SINGLE NEWS
# =========================
@router.get("/{news_id}", response_model=schemas.NewsResponse)
def get_single_news(news_id: int, db: Session = Depends(get_db)):

    news = db.query(models.News).filter(models.News.id == news_id).first()

    if not news:
        raise HTTPException(status_code=404, detail="News not found")

    return news