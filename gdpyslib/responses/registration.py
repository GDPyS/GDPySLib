from enum import IntEnum


class RegistrationResponse(IntEnum):
    SUCCESS = 1

    USERNAME_TAKEN = -2
    EMAIL_TAKEN = -3
    USERNAME_INVALID = -4
    PASSWORD_INVALID = -5
    EMAIL_INVALID = -6
    PASSWORDS_UNMATCHED = -7
    PASSWORD_TOO_SHORT = -8
    USERNAME_TOO_SHORT = -9
    EMAILS_UNMATCHED = -99

    def __str__(self) -> str:
        """str dundermethod for easy response returning"""
        return str(self.value)
