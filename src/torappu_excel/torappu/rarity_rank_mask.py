from ..common import CustomIntEnum


class RarityRankMask(CustomIntEnum):
    NONE = "NONE", 0
    TIER_1 = "TIER_1", 1
    TIER_2 = "TIER_2", 2
    TIER_3 = "TIER_3", 4
    TIER_4 = "TIER_4", 8
    TIER_5 = "TIER_5", 16
    TIER_6 = "TIER_6", 32
    ALL = "ALL", 63
