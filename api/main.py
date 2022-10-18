from fastapi import FastAPI

from api.routes import users

app = FastAPI()

app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
