from urllib.error import HTTPError
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from .models import tablemodels, schemas
from .database import SessionLocal, engine
import hashlib
from datetime import datetime

API_NAME = "Nerdy"


app = FastAPI()

tablemodels.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
         db.close()

@app.get("/", response_model=schemas.Health, status_code=status.HTTP_200_OK )
async def health():
    response = schemas.Health(apiName=API_NAME)
    return response



@app.post("/post/create/role", response_model=schemas.RoleResponse, status_code=status.HTTP_201_CREATED )
async def create_role(role: schemas.RoleRequest, db: Session = Depends(get_db)):


    new_role= tablemodels.Role(roletype=role.roletype, rolevalue=role.rolevalue, createdAt=datetime.timestamp(datetime.now()))
    db.add(new_role)
    db.commit()
    return {"data" : new_role}

@app.post("/post/create/user", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED )
async def create_user(user: schemas.UserRequest, db: Session = Depends(get_db)):
    print("działa")
    password  = hashlib.pbkdf2_hmac('sha256', user.password.encode('utf-8'),b'', 100000)
    
    stringPassword = str(password)
    if stringPassword == "":
        return HTTPException(status_code=404, detail="to do")
    
    new_user = tablemodels.User(username=user.username, password=stringPassword, createdAt=datetime.timestamp(datetime.now()))
    db.add(new_user)
    db.commit()
    return {"data" : "git"}