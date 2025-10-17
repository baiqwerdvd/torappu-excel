from .roguelike_activity_type import RoguelikeActivityType
from .roguelike_topic_mode import RoguelikeTopicMode
from ..common import BaseStruct


class RoguelikeActivityBasicData(BaseStruct):
    id: str
    type: RoguelikeActivityType
    startTime: int
    endTime: int
    isPresentSeedMode: bool
    isUnlockBadge: bool
    validMode: RoguelikeTopicMode
