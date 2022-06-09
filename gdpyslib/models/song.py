from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass
class Song:
    id: int
    name: str
    author_id: int
    author_name: int
    size: float # In MB
    disabled: bool
    song_url: str

    @classmethod
    def from_row(self, row: dict[str, Any]) -> Song:
        return Song(
            id=row["id"],
            name=row["name"],
            author_id=row["author_id"],
            author_name=row["author_name"],
            size=row["size"],
            disabled=row["disabled"],
            song_url=row["song_url"],
        )
