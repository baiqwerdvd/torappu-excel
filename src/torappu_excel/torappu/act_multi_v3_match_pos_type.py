from enum import IntEnum

from ..common import CustomIntEnum


class ActMultiV3MatchPosType(CustomIntEnum):
    NORMAL = "NORMAL", 0
    COACH = "COACH", 1
    STUDENT = "STUDENT", 2


class ActMultiV3MatchPosIntType(IntEnum):
    NORMAL = 0
    COACH = 1
    STUDENT = 2
