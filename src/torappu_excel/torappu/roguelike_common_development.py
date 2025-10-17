from .roguelike_common_development_effect_type import RoguelikeCommonDevelopmentEffectType
from .roguelike_common_development_node_type import RoguelikeCommonDevelopmentNodeType
from .roguelike_topic_display_item import RoguelikeTopicDisplayItem
from ..common import BaseStruct


class RoguelikeCommonDevelopment(BaseStruct):
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
