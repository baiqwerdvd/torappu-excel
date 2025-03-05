from enum import IntEnum, StrEnum


class DataUnlockType(StrEnum):
    DIRECT = "DIRECT"
    AWAKE = "AWAKE"
    FAVOR = "FAVOR"
    STAGE = "STAGE"
    ITEM = "ITEM"
    NEVER = "NEVER"
    PATCH = "PATCH"
    NONE = "NONE"


class DataUnlockTypeInt(IntEnum):
    DIRECT = 0
    AWAKE = 1
    FAVOR = 2
    STAGE = 3
    ITEM = 4
    NEVER = 5
    PATCH = 6
    NONE = 7
