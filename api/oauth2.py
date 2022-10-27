from uuid import uuid4
from fastapi_jwt_auth import AuthJWT

from api.schemas import TokenData


def create_auth_tokens(sub, fresh: bool = False):
    Authorize = AuthJWT()
    user_claims = {
        "auth_id": str(uuid4())
    }
    access_token = Authorize.create_access_token(subject=sub, fresh=fresh, user_claims=user_claims)
    # Critical user actions must use fresh_jwt_required()
    refresh_token = Authorize.create_refresh_token(subject=sub, user_claims=user_claims)
    return TokenData(access_token=access_token, refresh_token=refresh_token)
