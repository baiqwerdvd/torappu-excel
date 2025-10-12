from pydantic import BaseModel, ConfigDict

from .roguelike_event_type import RoguelikeEventType
from .roguelike_totem_blur_node_type import RoguelikeTotemBlurNodeType


class RoguelikeTotemLinkedNodeTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    effectiveNodeTypes: list[RoguelikeEventType]
    blurNodeTypes: list[RoguelikeTotemBlurNodeType]
