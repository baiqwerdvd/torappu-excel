from pydantic import BaseModel, ConfigDict

from .roguelike_event_type import RoguelikeEventType


class RoguelikeRollNodeData(BaseModel):
    class RoguelikeRollNodeGroupData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        nodeType: RoguelikeEventType

    zoneId: str
    groups: dict[str, "RoguelikeRollNodeData.RoguelikeRollNodeGroupData"]
