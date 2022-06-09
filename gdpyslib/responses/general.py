from enum import IntEnum

from gdpyslib.mixins.enum import StringCastMixin


class ResponseStatus(IntEnum, StringCastMixin):
    SUCCESS = 1
    FAIL = -1
