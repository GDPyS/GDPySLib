from motor.motor_asyncio import AsyncIOMotorClient

from gdpyslib.models.connection import Connection


class MongoConnection(Connection):
    def __init__(self, connection_info: str) -> None:
        self.connection_info: str = connection_info
        self.client: AsyncIOMotorClient = None

    async def connect(self) -> None:
        self.client = AsyncIOMotorClient(self.connection_info)

    async def disconnect(self) -> None:
        del self.client
