import motor.motor_asyncio
import certifi
from api.config import settings
from redis import Redis

mongodb_url = settings.mongodb_url
client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_url, tlsCAFile=certifi.where())


def get_db():
    db = client.fastapi_mongodb
    return db


redis_host = settings.redis_host
redis_port = settings.redis_port
redis_db = settings.redis_db
redis_conn = Redis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)
