from fastapi import FastAPI, Request
from api.routes import users, auth
from api.config import settings
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi_jwt_auth import AuthJWT

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


@AuthJWT.load_config
def get_config():
    return settings
