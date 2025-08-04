from sqlalchemy.orm import Session
from .models import JobApplication
from datetime import datetime

# Create new job application
def create_application(db: Session, data):
    application = JobApplication(**data)
    db.add(application)
    db.commit()
    db.refresh(application)
    return application

# Get all applications
def get_applications(db: Session):
    return db.query(JobApplication).all()

# Get single application by ID
def get_application(db: Session, app_id: int):
    return db.query(JobApplication).filter(JobApplication.id == app_id).first()

# Update existing application
def update_application(db: Session, app_id: int, data):
    app = get_application(db, app_id)
    for key, value in data.items():
        setattr(app, key, value)
    db.commit()
    return app

# Delete application
def delete_application(db: Session, app_id: int):
    app = get_application(db, app_id)
    db.delete(app)
    db.commit()
