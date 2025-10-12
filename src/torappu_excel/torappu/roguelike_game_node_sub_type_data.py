from pydantic import BaseModel, ConfigDict

from .roguelike_event_type import RoguelikeEventType


class RoguelikeGameNodeSubTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    eventType: RoguelikeEventType
    subTypeId: int
    iconId: str | None
    name: str | None
    description: str | None
