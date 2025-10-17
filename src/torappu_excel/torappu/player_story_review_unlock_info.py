from .story_review_unlock_info import StoryReviewUnlockInfo
from ..common import BaseStruct


class PlayerStoryReviewUnlockInfo(BaseStruct):
    rts: int
    stories: list[StoryReviewUnlockInfo]
    trailRewards: list[str] | None = None
