from pydantic import BaseModel, ConfigDict

from .roguelike_common_development_effect_type import RoguelikeCommonDevelopmentEffectType
from .roguelike_common_development_node_type import RoguelikeCommonDevelopmentNodeType
from .roguelike_topic_display_item import RoguelikeTopicDisplayItem


class RoguelikeCommonDevelopment(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buffId: str
    nodeType: RoguelikeCommonDevelopmentNodeType
    frontNodeId: list[str]
    nextNodeId: list[str]
    positionRow: int
    positionOrder: int
    tokenCost: int
    buffName: str
    activeIconId: str
    inactiveIconId: str
    bottomIconId: str
    effectType: RoguelikeCommonDevelopmentEffectType
    rawDesc: list[str]
    buffDisplayInfo: list[RoguelikeTopicDisplayItem]
    groupId: str
    enrollId: str | None
