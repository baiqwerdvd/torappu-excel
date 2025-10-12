from enum import StrEnum


class StorylineLocationType(StrEnum):
    STORY_SET = "STORY_SET"
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    MAINLINE_SPLIT = "MAINLINE_SPLIT"
