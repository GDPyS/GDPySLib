from enum import IntEnum


class ResponseStatus(IntEnum):
    SUCCESS = 1
    FAIL = -1

    def __str__(self) -> str:
        """str dundermethod for easy response returning"""
        return str(self.value)
