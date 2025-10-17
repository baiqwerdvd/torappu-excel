from .player_story_review_unlock_info import PlayerStoryReviewUnlockInfo
from ..common import BaseStruct


class PlayerStoryReview(BaseStruct):
    groups: dict[str, PlayerStoryReviewUnlockInfo]
    tags: dict[str, int]
