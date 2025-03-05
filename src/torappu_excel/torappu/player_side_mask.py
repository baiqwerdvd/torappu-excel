from enum import IntEnum


class PlayerSideMask(IntEnum):
    ALL = 0
    SIDE_A = 2
    SIDE_B = 4
    NONE = 255
