# Import libraries for database operations
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Base class for all database models
Base = declarative_base()

# Database model for job applications
class JobApplication(Base):
    __tablename__ = "applications"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Company name with index for faster searches
    company = Column(String, index=True)
    
    # Job position/title
    position = Column(String)
    
    # Current application status (Applied, Interview, etc.)
    status = Column(String)
    
    # When the application was submitted
    applied_date = Column(DateTime, default=datetime.utcnow)
    
    # Additional notes about the application
    notes = Column(String)