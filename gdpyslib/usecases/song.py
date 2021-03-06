from __future__ import annotations
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorDatabase
from gdpyslib.models.song import Song
from gdpyslib.usecases import web
from gdpyslib.constants import secrets

async def from_db(song_id: int, mongo: AsyncIOMotorDatabase) -> Optional[Song]:
    """Attempts to fetch a `Song` with the given `song_id` from the database."""

    song_db = await mongo.songs.find_one({"id": song_id})
    if not song_db:
        return None
    
    return Song.from_row(song_db)

async def from_gd(song_id: int) -> Optional[Song]:
    """Fetches the song data from the official Geometry Dash servers (over HTTP)."""

    # Using the Geometry Dash servers themselves as they have access to a private
    # Newgrounds API.
    resp = await web.post_boomlings("getGJSongInfo.php", {
        "secret": secrets.DEFAULT,
        "songID": song_id,
    })

    # Check if it is not an error message.
    if "~|~" not in resp:
        return None
    
    parsed_resp = web.parse_gd_dict(resp, "~|~")

    return Song(
        id=int(parsed_resp[1]),
        name=parsed_resp[2],
        author_id=int(parsed_resp[3]),
        author_name=parsed_resp[4],
        size=float(parsed_resp[5]),
        song_url=parsed_resp[10],
        disabled=False,
    )

async def insert(song: Song, mongo: AsyncIOMotorDatabase) -> None:
    """Inserts the song model `song` into the database."""

    await mongo.songs.insert_one(song.__dict__)

async def ensure(song_id: int, mongo: AsyncIOMotorDatabase) -> Optional[Song]:
    """Attempts to fetch the song from multiple sources, adding it to the
    database if not located in a local source."""

    song_db = await from_db(song_id, mongo)

    if song_db:
        return song_db
    
    # Crawling from GD servers.
    song_gd = await from_gd(song_id)

    if song_gd:
        # Add it to the database for future access.
        await insert(song_db, mongo)
    
    return song_gd
