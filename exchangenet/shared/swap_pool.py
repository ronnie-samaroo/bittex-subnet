from redis import asyncio as aioredis
import json

class SwapPool():
    """
    SwapPool is a simple redis based key value store for storing swap_id's.
    """

    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0):
        self.redis = aioredis.Redis(host=host, port=port, db=db)

    async def store(self, key: str, value):
        serialized_data = json.dumps(value) # Serialize the data before storing it.
        await self.redis.set(key, serialized_data)

    async def retrieve(self, key: str):
        serialized_data = await self.redis.get(key)
        # Deserialize the data before returning it.
        if serialized_data:
            return json.loads(serialized_data)
        else:
            return None

    async def delete(self, key: str):
        await self.redis.delete(key)

    async def exists(self, key: str) -> bool:
        return await self.redis.exists(key)

    async def clear(self):
        await self.redis.flushdb()

    async def close(self):
        self.redis.close()
        await self.redis.wait_closed()