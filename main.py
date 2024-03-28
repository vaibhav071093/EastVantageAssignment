from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from geopy.distance import geodesic
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize FastAPI
app = FastAPI()
