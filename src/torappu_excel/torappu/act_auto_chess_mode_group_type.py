from ..common import CustomIntEnum


class ActAutoChessModeGroupType(CustomIntEnum):
    GROUP_MULTI = "GROUP_MULTI", 0
    GROUP_ROOM = "GROUP_ROOM", 1
    GROUP_SINGLE = "GROUP_SINGLE", 2
    GROUP_FAST = "GROUP_FAST", 3
    GROUP_OFFSEASON = "GROUP_OFFSEASON", 4
