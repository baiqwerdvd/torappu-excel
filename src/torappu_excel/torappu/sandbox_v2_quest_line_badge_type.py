from enum import IntEnum

from ..common import CustomIntEnum


class SandboxV2QuestLineBadgeType(CustomIntEnum):
    NONE = "NONE", 0
    SIDE = "SIDE", 1
    GUIDE = "GUIDE", 2
    MAIN = "MAIN", 3
    RIFT = "RIFT", 4


class SandboxV2QuestLineBadgeTypeEnum(IntEnum):
    NONE = 0
    SIDE = 1
    GUIDE = 2
    MAIN = 3
    RIFT = 4
