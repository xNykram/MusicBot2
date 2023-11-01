import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.settings import config

engine = create_engine(config.POSTGRES_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()