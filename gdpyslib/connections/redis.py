import aioredis

from gdpyslib.models.connection import Connection


class RedisConnection(Connection):
    def __init__(self, connection_info: str) -> None:
        self.connection_info: str = connection_info
        self.client: aioredis.Redis = None

    async def connect(self) -> None:
        self.client = await aioredis.from_url(self.connection_info)

    async def disconnect(self) -> None:
        await self.client.close()
