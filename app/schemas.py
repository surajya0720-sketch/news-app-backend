from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NewsCreate(BaseModel):
    title: str
    content: str
    category: Optional[str] = None

class NewsResponse(NewsCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class AdminLogin(BaseModel):
    username: str
    password: str
