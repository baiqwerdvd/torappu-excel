from ..common import CustomIntEnum


class StageDiffGroup(CustomIntEnum):
    NONE = "NONE", 0
    EASY = "EASY", 1
    NORMAL = "NORMAL", 2
    TOUGH = "TOUGH", 4
    ALL = "ALL", 7
