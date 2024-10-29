from pydantic import BaseModel, EmailStr, Field, HttpUrl
from datetime import datetime, date
from typing import Optional, List

# User Schemas
class UserBase(BaseModel):
    first_name: str = Field(..., example="John")
    last_name: str = Field(..., example="Doe")
    birth_date: date = Field(..., example="1990-01-01")
    email: EmailStr = Field(..., example="john.doe@example.com")
    phone_number: str = Field(..., example="1234567890")

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, example="strongpassword")

class UserLogin(BaseModel):
    email: EmailStr = Field(..., example="john.doe@example.com")
    password: str = Field(..., min_length=8, example="strongpassword")

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True

# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    email: EmailStr

class TokenData(BaseModel):
    email: Optional[EmailStr] = None

# Permission Schemas
class PermissionBase(BaseModel):
    user_id: int
    backend_access: str = Field(..., example="All")

class PermissionCreate(PermissionBase):
    pass

class PermissionResponse(PermissionBase):
    id: int

    class Config:
        orm_mode = True
