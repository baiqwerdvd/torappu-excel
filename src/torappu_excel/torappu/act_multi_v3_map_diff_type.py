from ..common import CustomIntEnum


class ActMultiV3MapDiffType(CustomIntEnum):
    NONE = "NONE", 0
    TRAINING = "TRAINING", 1
    ORDINARY = "ORDINARY", 2
    DIFFICULTY = "DIFFICULTY", 3
    EXTREMELY = "EXTREMELY", 4
