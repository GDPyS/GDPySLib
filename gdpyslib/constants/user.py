import re
from enum import IntFlag


class RequestStatus(IntFlag):
    """Profile statuses on whether eg friend reqs are enabled."""

    MESSAGES = 1 << 0
    REQUESTS = 1 << 1
    COMMENTS = 1 << 2
    MESSAGES_FRIENDS_ONLY = 1 << 3
    COMMENTS_FRIENDS_ONLY = 1 << 4


class Privileges(IntFlag):
    """The GDPyS privileges."""

    LOGIN = 1 << 0
    PUBLIC = 1 << 1
    COMMENT = 1 << 2
    LEVEL_UPL = 1 << 3
    RATE = 1 << 4
    MOD_BADGE = 1 << 5
    ELDER_BADGE = 1 << 6
    SUPPORTER = 1 << 7
    DEV_DEBUG = 1 << 8


EMAIL_REGEX = re.compile(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
