from typing import Any


class Connection:
    """Generic type-hinting class for connections"""

    connection_info: Any
    client: Any

    async def connect(self) -> None:
        ...

    async def disconnect(self) -> None:
        ...

    def __getattr__(self, __name: str) -> Any:
        return self.client.__getattr__(__name)
