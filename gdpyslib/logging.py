import sys
import time
from enum import IntEnum
from typing import Optional
from typing import Union


def formatted_time() -> str:
    return time.strftime("%I:%M:%S%p", time.localtime())


class Ansi(IntEnum):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37

    GRAY = 90
    LRED = 91
    LGREEN = 92
    LYELLOW = 93
    LBLUE = 94
    LMAGENTA = 95
    LCYAN = 96
    LWHITE = 97

    RESET = 0

    def __repr__(self) -> str:
        return f"\x1b[{self.value}m"


def _log(content: str, log_type: str, colour: Ansi = Ansi.WHITE) -> None:
    """Logs a message to stdout with a given Ansi colour."""

    log_type = log_type.rjust(5)
    sys.stdout.write(
        f"\033[37m{Ansi.GRAY!r}\033[49m[{formatted_time()} - {log_type}]"
        f"\033[37m{colour!r}\033[49m {content}"
        "\033[39m\n",
    )


def debug(message: str, file: Optional[str] = None) -> None:
    _log(message, "DEBUG", Ansi.LGREEN)

    if file:
        with open(file, "a+") as f:
            f.write(f"[{formatted_time()} - DEBUG] {message}\n")


def info(message: str, file: Optional[str] = None) -> None:
    _log(message, "INFO", Ansi.LBLUE)

    if file:
        with open(file, "a+") as f:
            f.write(f"[{formatted_time()} - INFO] {message}\n")


def error(message: str, file: Optional[str] = None) -> None:
    _log(message, "ERROR", Ansi.LRED)

    if file:
        with open(file, "a+") as f:
            f.write(f"[{formatted_time()} - ERROR] {message}\n")


def warning(message: str, file: Optional[str] = None) -> None:
    _log(message, "WARN", Ansi.LYELLOW)

    if file:
        with open(file, "a+") as f:
            f.write(f"[{formatted_time()} - WARN] {message}\n")


TIME_ORDER_SUFFIXES = ["ns", "μs", "ms", "s"]


def format_time(time: Union[int, float]) -> str:
    for suffix in TIME_ORDER_SUFFIXES:
        if time < 1000:
            break

        time /= 1000

    return f"{time:.2f}{suffix}"
