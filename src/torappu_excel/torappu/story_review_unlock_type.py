from enum import StrEnum


class StoryReviewUnlockType(StrEnum):
    STAGE_CLEAR = "STAGE_CLEAR"
    USE_ITEM = "USE_ITEM"
    BY_START_TIME = "BY_START_TIME"
    NOTHING = "NOTHING"
