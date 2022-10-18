from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId


class User(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "kiarash",
                "email": "kiarash@kiarash.com",
                "password": "secret"
            }
        }
