from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.errors import NetworkTimeout
from fastapi_jwt_auth import AuthJWT
from api import schemas
from api.database import get_db

router = APIRouter(
    tags=["User routes"],
    prefix="/users"
)


@router.get('/me', status_code=status.HTTP_200_OK, response_model=schemas.UserResponse)
async def get_me(Authorize: AuthJWT = Depends(), db=Depends(get_db)):
    Authorize.jwt_required()
    current_user_id = Authorize.get_jwt_subject()
    try:
        current_user = await db.users.find_one({'_id': current_user_id})
    except NetworkTimeout:
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="Request timed out.")
    return current_user
