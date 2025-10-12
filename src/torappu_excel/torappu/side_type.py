from enum import StrEnum


class SideType(StrEnum):
    NONE = "NONE"
    ALLY = "ALLY"
    ENEMY = "ENEMY"
    BOTH_ALLY_AND_ENEMY = "BOTH_ALLY_AND_ENEMY"
    NEUTRAL = "NEUTRAL"
    ALL = "ALL"
