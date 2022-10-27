from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId


class UserBase(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)


class UserRegister(UserBase):
    id: str = Field(default_factory=ObjectId, alias="_id")
    password: str = Field(...)

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "username": "kiarash",
                "email": "kiarash@kiarash.com",
                "password": "secret"
            }
        }


class UserResponse(UserBase):
    id: str = Field(default_factory=ObjectId, alias="_id")

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "_id": "id",
                "username": "kiarash",
                "email": "kiarash@kiarash.com",
            }
        }


class UserLogin(BaseModel):
    identifier: str = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class TokenData(BaseModel):
    type: str = "Bearer"
    access_token: str
    refresh_token: str
