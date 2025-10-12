from pydantic import BaseModel, ConfigDict, Field

from .item_bundle import ItemBundle
from .roguelike_topic_challenge_task import RoguelikeTopicChallengeTask


class RoguelikeTopicChallenge(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    challengeId: str
    sortId: int
    challengeName: str
    challengeGroup: int
    challengeGroupSortId: int
    challengeGroupName: str | None
    challengeUnlockDesc: str | None
    challengeUnlockToastDesc: str | None
    challengeDes: str
    challengeConditionDes: list[str]
    challengeTasks: dict[str, RoguelikeTopicChallengeTask]
    defaultTaskId: str
    rewards: list[ItemBundle]
    challengeStoryId: str | None = Field(default=None)
    taskDes: str | None = Field(default=None)
    completionClass: str | None = Field(default=None)
    completionParams: list[str] | None = Field(default=None)
