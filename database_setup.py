# database_setup.py

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class WeatherSummary(Base):
    __tablename__ = 'weather_summary'

    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    temperature = Column(Float, nullable=False)
    weather_condition = Column(String, nullable=False)


# Connect to SQLite database (creates a file named weather_data.db)
engine = create_engine('sqlite:///weather_data.db')
Session = sessionmaker(bind=engine)

# Create tables
Base.metadata.create_all(engine)
