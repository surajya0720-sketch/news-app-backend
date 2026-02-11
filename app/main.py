from fastapi import FastAPI
from app.database import engine, Base
from app.routes import router

app = FastAPI(title="News App API")

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "News App Backend is running"}