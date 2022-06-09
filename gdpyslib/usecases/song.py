from __future__ import annotations
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorDatabase
from gdpyslib.models.song import Song

async def from_db(song_id: int, mongo: AsyncIOMotorDatabase) -> Optional[Song]:
    """Attempts to fetch a `Song` with the given `song_id` from the database."""

    song_db = await mongo.songs.find_one({"id": song_id})
    if not song_db:
        return None
    
    return Song.from_row(song_db)

async def from_gd(song_id: int) -> Optional[Song]:
    """Fetches the song data from the official Geometry Dash servers (over HTTP)."""

    # TODO: Just establishing the naming conventions.
    ...

async def insert(song: Song, mongo: AsyncIOMotorDatabase) -> None:
    """Inserts the song model `song` into the database."""

    await mongo.songs.insert_one(song.__dict__)
