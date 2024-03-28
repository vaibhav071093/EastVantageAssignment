from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, engine
from api import router as api_router

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency for database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Include API routes
app.include_router(api_router)
