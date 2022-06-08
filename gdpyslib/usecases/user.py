import time
from typing import Optional
from typing import Union

from motor.motor_asyncio import AsyncIOMotorDatabase

from gdpyslib.constants.user import EMAIL_REGEX
from gdpyslib.constants.user import Privileges
from gdpyslib.constants.user import RequestStatus
from gdpyslib.cryptography.bcrypt import hash_bcrypt
from gdpyslib.models.user import User
from gdpyslib.responses.registration import RegistrationResponse

KWARGS_VALUES = Union[int, str]


def _parse_kwargs(
    kwargs: dict[str, KWARGS_VALUES],
) -> Optional[tuple[str, KWARGS_VALUES]]:
    for kwarg in ("id", "name"):
        if val := kwargs.pop(kwarg, None):
            return (kwarg, val)

    return None


async def fetch_user(**kwargs) -> Optional[User]:
    """Fetches a GDPyS user from the database via name or ID"""
    mongo: AsyncIOMotorDatabase = kwargs["mongo"]
    if not (kwarg := _parse_kwargs(kwargs)):
        raise ValueError("Incorrect parameters passed to fetch_user()")

    key, val = kwarg
    row = await mongo.users.find_one({key: val})
    if not row:
        return None

    return User.from_row(row)


async def register_user(
    name: str,
    email: str,
    password: str,
    mongo: AsyncIOMotorDatabase,
) -> tuple[RegistrationResponse, Optional[User]]:
    """Attempts to register a user into the GDPyS database, with a given response and optionally the new user object"""
    name_exists = await mongo.users.find_one({"name": name})
    if name_exists:
        return (RegistrationResponse.USERNAME_TAKEN, None)

    email_exists = await mongo.users.find_one({"email": email})
    if email_exists:
        return (RegistrationResponse.EMAIL_TAKEN, None)

    if not EMAIL_REGEX.match(email):
        return (RegistrationResponse.EMAIL_INVALID, None)

    if len(name) < 3:
        return (RegistrationResponse.USERNAME_TOO_SHORT, None)

    if len(name) > 16:
        return (RegistrationResponse.USERNAME_INVALID, None)

    if len(password) < 6:
        return (RegistrationResponse.PASSWORD_TOO_SHORT, None)

    password_bcrypt = await hash_bcrypt(password)

    # not proud of this...
    current_highest_userid = mongo.users.find().sort("id", -1).limit(1)
    users = [user async for user in current_highest_userid]
    user_id = users[0]["id"] + 1 if users else 1

    user_info = {
        "id": user_id,
        "name": name,
        "privileges": Privileges.PUBLIC,
        "email": email,
        "password_bcrypt": password_bcrypt,
        "register_timestamp": int(time.time()),
        "youtube_url": "",
        "twitter_url": "",
        "twitch_url": "",
        "request_status": RequestStatus.REQUESTS,
    }

    await mongo.users.insert_one(user_info)
    return (RegistrationResponse.SUCCESS, User.from_row(user_info))
