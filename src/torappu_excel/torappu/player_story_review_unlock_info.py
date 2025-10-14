from pydantic import BaseModel, ConfigDict

from .story_review_unlock_info import StoryReviewUnlockInfo


class PlayerStoryReviewUnlockInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rts: int
    stories: list[StoryReviewUnlockInfo]
    trailRewards: list[str] | None = None
