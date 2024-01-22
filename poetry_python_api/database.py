import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()
SQLALCHEMY_DATABSE_URL = os.getenv("SQLALCHEMY_DATABSE_URL")

engine = create_engine(
    SQLALCHEMY_DATABSE_URL,
    connect_args={"check_same_thread": False},
    echo=True,  # PROD: False
)

SessionLocal = sessionmaker(bind=engine)
