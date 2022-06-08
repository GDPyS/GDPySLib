from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from gdpyslib.constants.user import Privileges
from gdpyslib.constants.user import RequestStatus


@dataclass
class User:
    id: int
    name: str

    privileges: Privileges
    email: str
    password_bcrypt: str

    register_timestamp: int
    youtube_url: str
    twitter_url: str
    twitch_url: str

    request_status: RequestStatus

    @classmethod
    def from_row(self, row: dict[str, Any]) -> User:
        return User(
            id=row["id"],
            name=row["name"],
            privileges=Privileges(row["privileges"]),
            email=row["email"],
            password_bcrypt=row["password_bcrypt"],
            register_timestamp=row["register_timestamp"],
            youtube_url=row["youtube_url"],
            twitter_url=row["twitter_url"],
            twitch_url=row["twitch_url"],
            request_status=RequestStatus(row["request_status"]),
        )
