from ..common import CustomIntEnum


class OccPer(CustomIntEnum):
    ALWAYS = "ALWAYS", 0
    ALMOST = "ALMOST", 1
    USUAL = "USUAL", 2
    OFTEN = "OFTEN", 3
    SOMETIMES = "SOMETIMES", 4
    NEVER = "NEVER", 5
    DEFINITELY_BUFF = "DEFINITELY_BUFF", 6
