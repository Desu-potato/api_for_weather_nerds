from pydantic import BaseModel, EmailStr
from typing import Optional


class AdditionalInfo(BaseModel):
      id : str
      createdAt : str

class Health(BaseModel):
    apiName : Optional[str]


class UserRequest(BaseModel):
    email : EmailStr
    username : str
    password : str

class UserResponse(BaseModel):
    userid : str

class RoleRequest(BaseModel):
    roletype : str
    rolevalue : int

class RoleResponse(BaseModel):
    roleid : str
  

class UserLoginRequest(BaseModel):
    username : str
    password : str

class UserLoginResponse(BaseModel):
    token : str
    tokentype : str
