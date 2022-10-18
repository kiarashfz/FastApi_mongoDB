from fastapi import APIRouter

router = APIRouter(
    tags=["User routes"]
)


@router.get("/")
async def root():
    return {"message": "Hello User"}
