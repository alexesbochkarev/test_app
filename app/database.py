from redis import Redis
from redis import ConnectionError as RedisConnectionError

from app.config import settings


redis_client = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True,
    password=settings.REDIS_PASSWORD,
)

try:
    redis_conn = redis_client.info()
    print(f'Connected to Redis {redis_conn.get("redis_version")}')
except RedisConnectionError as e:
    raise ConnectionError("Unable to connect to Redis")
except Exception as e:
    raise e
