from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from ..models import tablemodels, schemas
from ..database import get_db
from ..helpers import hash
import hashlib

SALT = b'Bec0n'



router = APIRouter()


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



@router.post("/create/user", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED )
async def create_user(user: schemas.UserRequest, db: Session = Depends(get_db)):
    testList = db.query(tablemodels.User).filter(tablemodels.User.username == user.username, tablemodels.User.email == user.email).first()
    if bool(testList):
        raise HTTPException(status_code=404, detail="to do")

    new_user = tablemodels.User(email=user.email, username=user.username, password=hash(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return schemas.UserResponse(userid = str(new_user.id))