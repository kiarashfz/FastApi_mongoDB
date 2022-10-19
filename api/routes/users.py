from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from pymongo.errors import DuplicateKeyError

from api import schemas
from api.database import db
from api.utils import password_hasher

router = APIRouter(
    tags=["User routes"]
)


@router.post('/sign-up', status_code=status.HTTP_201_CREATED, response_description='User successfully registered.',
             response_model=schemas.UserResponse)
async def sign_up(user: schemas.User, mongodb=Depends(db)):
    try:
        user.password = password_hasher(user.password)
        user = jsonable_encoder(user)
        await mongodb.users.insert_one(user)
        return user
    # username & email fields have unique indexes so DuplicateKeyError may be raised
    except DuplicateKeyError as e:
        error_field_name = next(iter(e.details["keyPattern"]))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'{error_field_name.title()} already exists.')
