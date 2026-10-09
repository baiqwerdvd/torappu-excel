from ..common import CustomIntEnum


class RoguelikeMoveScrapRangeType(CustomIntEnum):
    RANGE = "RANGE", 0
    FULL_MAP = "FULL_MAP", 1
    FULL_ROW_COL = "FULL_ROW_COL", 2
