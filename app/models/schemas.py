from pydantic import BaseModel
from typing import Optional

class Health(BaseModel):
    apiName : Optional[str]


class UserRequest(BaseModel):
    username : str
    password : str

class UserResponse(BaseModel):
    userid : str

class RoleRequest(BaseModel):
    roletype : str
    rolevalue : int

class RoleResponse(BaseModel):
    roleid : str
  

