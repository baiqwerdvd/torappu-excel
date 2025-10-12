from pydantic import BaseModel, ConfigDict

from .roguelike_activity_type import RoguelikeActivityType
from .roguelike_topic_mode import RoguelikeTopicMode


class RoguelikeActivityBasicData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: RoguelikeActivityType
    startTime: int
    endTime: int
    isPresentSeedMode: bool
    isUnlockBadge: bool
    validMode: RoguelikeTopicMode
