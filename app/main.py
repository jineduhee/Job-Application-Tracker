# Import required libraries
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from . import crud, models, database
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

# Create database tables
models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

# Database session dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Data validation models
class JobAppSchema(BaseModel):
    company: str
    position: str
    status: str
    notes: str

class URLSchema(BaseModel):
    url: str

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Main page
@app.get("/", response_class=FileResponse)
def read_index():
    return FileResponse(os.path.join("static", "index.html"))

# API endpoints for CRUD operations
@app.post("/applications/")
def create_app(app_data: JobAppSchema, db: Session = Depends(get_db)):
    return crud.create_application(db, app_data.dict())

@app.get("/applications/")
def read_apps(db: Session = Depends(get_db)):
    return crud.get_applications(db)

@app.put("/applications/{app_id}")
def update_app(app_id: int, app_data: JobAppSchema, db: Session = Depends(get_db)):
    return crud.update_application(db, app_id, app_data.dict())

@app.delete("/applications/{app_id}")
def delete_app(app_id: int, db: Session = Depends(get_db)):
    crud.delete_application(db, app_id)
    return {"message": "Deleted"}