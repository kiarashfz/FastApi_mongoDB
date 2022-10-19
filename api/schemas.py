from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId


class User(BaseModel):
    id: str = Field(default_factory=ObjectId, alias="_id")
    username: str = Field(...)
    email: EmailStr = Field(...)
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


class UserResponse(BaseModel):
    id: str = Field(default_factory=ObjectId, alias="_id")
    username: str = Field(...)
    email: EmailStr = Field(...)

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
