from enum import IntEnum


class PlayerBuildingTraineeState(IntEnum):
    EMPTY = 0
    TRAINING = 1
    OUTOFDATE = 2
    WAITING = 3
