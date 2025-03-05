from enum import IntEnum, StrEnum


class BuildableType(IntEnum):
    NONE = 0
    MELEE = 1
    RANGED = 2
    ALL = 3


class BuildableTypeStr(StrEnum):
    NONE = "NONE"
    MELEE = "MELEE"
    RANGED = "RANGED"
    ALL = "ALL"
