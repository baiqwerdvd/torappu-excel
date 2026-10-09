from ..common import CustomIntEnum


class ArkventTaskVarSeqCompareOperation(CustomIntEnum):
    NONE = "NONE", 0
    GT = "GT", 1
    GE = "GE", 2
    EQ = "EQ", 3
    NEQ = "NEQ", 4
    LE = "LE", 5
    LT = "LT", 6
