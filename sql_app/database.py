# Import the SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a database URL for SQLAlchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# In this app we're  using SQLite
# If you were using a PostgreSQL database instead, you would just have to uncomment the line:
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)