from enum import IntEnum

from gdpyslib.mixins.enum_casts import StringCastMixin


class ResponseStatus(IntEnum, StringCastMixin):
    SUCCESS = 1
    FAIL = -1
