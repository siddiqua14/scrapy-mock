import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(String, nullable=False)
    url = Column(String, nullable=False)
    image_path = Column(String, nullable=False)

# Use the DATABASE_URL environment variable for database connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://scraper_user:scraper_password@localhost:5432/scraper_db")
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
