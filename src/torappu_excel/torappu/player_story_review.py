from pydantic import BaseModel, ConfigDict

from .player_story_review_unlock_info import PlayerStoryReviewUnlockInfo


class PlayerStoryReview(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groups: dict[str, PlayerStoryReviewUnlockInfo]
    tags: dict[str, int]
