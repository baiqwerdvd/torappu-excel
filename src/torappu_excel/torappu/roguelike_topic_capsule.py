from pydantic import BaseModel, ConfigDict

from .roguelike_event_type import RoguelikeEventType


class RoguelikeTopicCapsule(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    maskType: RoguelikeEventType
    innerColor: str
