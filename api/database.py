import motor.motor_asyncio
import certifi
from api.config import settings

mongodb_url = settings.mongodb_url
client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_url, tlsCAFile=certifi.where())


def get_db():
    db = client.fastapi_mongodb
    return db
