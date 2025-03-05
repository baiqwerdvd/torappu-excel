from .item_bundle import ItemBundle
from .roguelike_topic_challenge_task import RoguelikeTopicChallengeTask
from ..common import BaseStruct

from msgspec import field


class RoguelikeTopicChallenge(BaseStruct):
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
    challengeStoryId: str | None = field(default=None)
    taskDes: str | None = field(default=None)
    completionClass: str | None = field(default=None)
    completionParams: list[str] | None = field(default=None)
