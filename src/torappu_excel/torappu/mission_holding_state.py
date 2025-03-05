from enum import IntEnum


class MissionHoldingState(IntEnum):
    NOT_OPEN = 0
    IN_EFFECT = 1
    CONFIRMED = 2
    FINISHED = 3
