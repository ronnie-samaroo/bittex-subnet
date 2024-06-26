import os
import json

from redis import asyncio as aioredis
from dotenv import load_dotenv
from collections import deque
from datetime import datetime


load_dotenv()

REDIS_SERVER_HOST = os.getenv('REDIS_SERVER_HOST', 'localhost')
REDIS_SERVER_PORT = os.getenv('REDIS_SERVER_PORT', 6379)
REDIS_DB = os.getenv('REDIS_DB', 1)
REDIS_SERVER_PASSWORD = os.getenv('REDIS_SERVER_PASSWORD', None)

class ValidatorStorage():
    """
    The ValidatorStorage class provides functionality for validators to store `swap_id`s. 

    As a default, it uses Redis as a backend and provides methods for storing, retrieving, and managing data.
    """

    def __init__(self):
        self.redis = aioredis.Redis(host=REDIS_SERVER_HOST, port=REDIS_SERVER_PORT, db=REDIS_DB, password=REDIS_SERVER_PASSWORD, decode_responses=True)
        self.pool_name = 'validator_swaps'
        self.hotkeys_pool_name = 'hotkeys'
    
    async def store_swap(self, swap_id: str, swap_info: str):
        return await self.redis.hset(self.pool_name, swap_id, json.dumps(swap_info))

    async def retrieve_swap(self, swap_id: str):
        value = await self.redis.hget(self.pool_name, swap_id)
        return json.loads(value) if value else None

    async def retrieve_swaps(self):
        return await self.redis.hkeys(self.pool_name)

    async def delete_swap(self, swap_id: str):
        await self.redis.hdel(self.pool_name, swap_id)

    async def clear_swaps(self):
        keys = await self.redis.hkeys(self.pool_name)
        if keys:
            await self.redis.hdel(self.pool_name, *keys)

    async def store_hotkey(self, account_address: str, hotkey: str):
        return await self.redis.hset(self.hotkeys_pool_name, account_address, hotkey)

    async def retrieve_hotkey(self, account_address: str):
        return await self.redis.hget(self.hotkeys_pool_name, account_address)

    async def delete_hotkey(self, swap_id: str):
        await self.redis.hdel(self.hotkeys_pool_name, swap_id)

    async def store_total_stats(self, hotkey: str, field_name: str, value: int):
        return await self.redis.hset(hotkey, field_name, value)
    
    async def retrieve_total_stats(self, hotkey: str, field_name: str):
        if await self.redis.hexists(hotkey, field_name):
            return await self.redis.hget(hotkey, field_name)
        return 0

    async def store_weekly_stats(self, hotkey: str, field_name: str, value: deque):
        serialized_deque = json.dumps(list(value))
        return await self.redis.hset(hotkey, field_name, serialized_deque)

    async def retrieve_weekly_stats(self, hotkey: str, field_name: str):
        if await self.redis.hexists(hotkey, field_name):
            loaded_list = json.loads(await self.redis.hget(hotkey, field_name))
            return deque(loaded_list)
        return deque([{datetime.now().date().toordinal(): 0}])
