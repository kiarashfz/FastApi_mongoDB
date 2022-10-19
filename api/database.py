import motor.motor_asyncio

from api.config import settings

mongodb_url = settings.mongodb_url
client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_url)

db = client.fastapi_mongodb
users_collection = db.get_collection("users")
