from ..common import CustomIntEnum


class OpenServerV3JumpType(CustomIntEnum):
    NONE = "NONE", 0
    MAIN_STAGE = "MAIN_STAGE", 1
    CHAR_REPO = "CHAR_REPO", 2
    WEEKLY = "WEEKLY", 3
    SHOP = "SHOP", 4
    BUILDING = "BUILDING", 5
    CAMPAIGN_STAGE = "CAMPAIGN_STAGE", 6
