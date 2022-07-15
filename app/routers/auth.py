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
    


@router.post("/create/role", response_model=schemas.RoleResponse, status_code=status.HTTP_201_CREATED )
async def create_role(role: schemas.RoleRequest, db: Session = Depends(get_db)):
    testList = db.query(tablemodels.Role).filter(tablemodels.Role.roletype == role.roletype).first()
    if bool(testList):
        raise HTTPException(status_code=404, detail="to do")

    testList = db.query(tablemodels.Role).filter(tablemodels.Role.roletype == role.roletype, tablemodels.Role.rolevalue == role.rolevalue).first()
    if bool(testList):
        raise HTTPException(status_code=404, detail="to do")

    new_role= tablemodels.Role(roletype=role.roletype, rolevalue=role.rolevalue)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return schemas.RoleResponse(roleid=str(new_role.id))
