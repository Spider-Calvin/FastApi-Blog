from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace 'username', 'password', 'database_name' with your actual AWS RDS PostgreSQL credentials
SQLALCHEMY_DATABASE_URL = 'postgresql://spider_calvin:AkjasdiiKJHDSjdjhanJHDJNjhas@database-1.c7eku8mq8cw9.ap-south-1.rds.amazonaws.com:5432/postgres'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
