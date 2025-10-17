from enum import IntEnum

from ..common import CustomIntEnum


class SandboxV2NodeType(CustomIntEnum):
    NONE = "NONE", 0
    HOME = "HOME", 1
    HOME_OUTPOST = "HOME_OUTPOST", 2
    BATTLE = "BATTLE", 3
    NEST = "NEST", 4
    COLLECT = "COLLECT", 5
    HUNT = "HUNT", 6
    CAVE = "CAVE", 7
    MINE = "MINE", 8
    ENCOUNTER = "ENCOUNTER", 9
    EXPEDITION = "EXPEDITION", 10
    SHOP = "SHOP", 11
    GATE = "GATE", 12
    MARKET = "MARKET", 13
    HOME_PORTABLE = "HOME_PORTABLE", 14
    HOME_PORTABLE_RIFT = "HOME_PORTABLE_RIFT", 15
    SELECTION = "SELECTION", 16
    RACING = "RACING", 17


class SandboxV2NodeTypeEnum(IntEnum):
    NONE = 0
    HOME = 1
    HOME_OUTPOST = 2
    BATTLE = 3
    NEST = 4
    COLLECT = 5
    HUNT = 6
    CAVE = 7
    MINE = 8
    ENCOUNTER = 9
    EXPEDITION = 10
    SHOP = 11
    GATE = 12
    MARKET = 13
    HOME_PORTABLE = 14
    HOME_PORTABLE_RIFT = 15
    SELECTION = 16
    RACING = 17
