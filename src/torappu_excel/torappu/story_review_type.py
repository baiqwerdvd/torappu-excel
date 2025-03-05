from ..common import CustomIntEnum


class StoryReviewType(CustomIntEnum):
    NONE = "NONE", 0
    ACTIVITY_STORY = "ACTIVITY_STORY", 1
    MINI_STORY = "MINI_STORY", 2
    MAIN_STORY = "MAIN_STORY", 3
