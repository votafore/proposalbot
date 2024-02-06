from enum import Enum
from typing import Final


class MessageTypes(Enum):
    PING = 1
    SHOW = 2
    DELETE = 3
    LIST = 4


class Result(Enum):
    OK = 1
    IN_PROGRESS = 2
    FAILURE = 3
    ERROR = 4


phone_number_length: Final[int] = 12
