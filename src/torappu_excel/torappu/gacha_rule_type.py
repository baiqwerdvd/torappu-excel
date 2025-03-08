from ..common import CustomIntEnum


class GachaRuleType(CustomIntEnum):
    NORMAL = "NORMAL", 0
    LIMITED = "LIMITED", 1
    LINKAGE = "LINKAGE", 2
    ATTAIN = "ATTAIN", 3
    CLASSIC = "CLASSIC", 4
    SINGLE = "SINGLE", 5
    FESCLASSIC = "FESCLASSIC", 6
    CLASSIC_ATTAIN = "CLASSIC_ATTAIN", 7
    SPECIAL = "SPECIAL", 8
    DOUBLE = "DOUBLE", 9
    CLASSIC_DOUBLE = "CLASSIC_DOUBLE", 10
