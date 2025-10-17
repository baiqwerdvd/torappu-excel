from enum import IntEnum


class PlayerBuildingTrainerState(IntEnum):
    EMPTY = 0
    TRAINING = 1
    FINISH = 2
    WAITING = 3
