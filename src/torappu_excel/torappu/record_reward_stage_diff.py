from ..common import CustomIntEnum


class RecordRewardStageDiff(CustomIntEnum):
    NONE = "NONE", 0
    EASY = "EASY", 1
    NORMAL = "NORMAL", 2
    TOUGH = "TOUGH", 3
    PREDEFINED = "PREDEFINED", 4
    HARD = "HARD", 5
