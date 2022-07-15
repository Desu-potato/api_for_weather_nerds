from os import access
from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from ..models import schemas, tablemodels
from ..database import get_db
from ..helpers import verify

from jose import jwt
from datetime import datetime, timedelta

router = APIRouter(tags=['Authentication'])






SECRET = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
ACCES_TIME = 15

def create_acces_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_token = jwt.encode(to_encode, SECRET, algorithm="HS256")
    return encoded_token


@router.post('/login', response_model=schemas.UserLoginResponse, status_code=status.HTTP_201_CREATED)
def login(user: schemas.UserLoginRequest , db: Session = Depends(get_db)):
    userRecord = db.query(tablemodels.User).filter(tablemodels.User.username == user.username).first()
    if not userRecord:
        raise HTTPException(status_code=401, detail="to do")
   
    passwd = verify(user.password, userRecord.password)
    if not passwd:
        raise HTTPException(status_code=404, detail="to do")

   
    access_token = create_acces_token(data={"user_id": str(userRecord.id)})
    return schemas.UserLoginResponse(token=access_token, tokentype="bearer")
    
