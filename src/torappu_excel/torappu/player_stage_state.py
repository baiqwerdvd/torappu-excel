from enum import IntEnum, StrEnum


class PlayerStageState(IntEnum):
    UNLOCKED = 0
    PLAYED = 1
    PASS = 2
    COMPLETE = 3


class PlayerStageStateStrEnum(StrEnum):
    UNLOCKED = "UNLOCKED"
    PLAYED = "PLAYED"
    PASS = "PASS"
    COMPLETE = "COMPLETE"
