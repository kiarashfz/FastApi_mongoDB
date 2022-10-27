from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from pymongo.errors import DuplicateKeyError, NetworkTimeout
from fastapi_jwt_auth import AuthJWT
import re
from api import schemas
from api.config import settings
from api.database import get_db, redis_conn
from api.oauth2 import create_auth_tokens
from api.utils import password_hasher, verify_password

router = APIRouter(
    tags=["Authentication"],
    prefix="/auth"
)


@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(decrypted_token):
    auth_id = decrypted_token['auth_id']
    entry = redis_conn.get(auth_id)
    return entry and entry == 'true'


@router.post('/sign-up', status_code=status.HTTP_201_CREATED, response_description='User successfully registered.',
             response_model=schemas.TokenData)
async def sign_up(user: schemas.UserRegister, db=Depends(get_db)):
    try:
        user.password = password_hasher(user.password)
        user = jsonable_encoder(user)
        await db.users.insert_one(user)
        token = create_auth_tokens(user['_id'], fresh=True)
        return token
    # username & email fields have unique indexes so DuplicateKeyError may be raised
    except DuplicateKeyError as e:
        error_field_name = next(iter(e.details["keyPattern"]))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'{error_field_name.title()} already exists.')
    except NetworkTimeout:
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="Request timed out.")


@router.post('/login', status_code=status.HTTP_200_OK, response_model=schemas.TokenData)
async def login(user: schemas.UserLogin, db=Depends(get_db)):
    email_regex_pattern = settings.email_regex
    username_regex_pattern = settings.username_regex
    found_user = None
    try:
        if re.fullmatch(email_regex_pattern, user.identifier):
            found_user = await db.users.find_one({"email": user.identifier})
        elif re.fullmatch(username_regex_pattern, user.identifier):
            found_user = await db.users.find_one({"username": user.identifier})
    except NetworkTimeout:
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="Request timed out.")

    if not found_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User and password doesn't match.")
    elif verify_password(user.password, found_user['password']):
        token = create_auth_tokens(found_user['_id'], fresh=True)
        return token


@router.post('/refresh')
async def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()
    current_user_id = Authorize.get_jwt_subject()
    auth_id = Authorize.get_raw_jwt()['auth_id']
    redis_conn.setex(auth_id, settings.authjwt_refresh_token_expires, 'true')
    token = create_auth_tokens(current_user_id)
    return token
