from .rl03_development_effect_type import RL03DevelopmentEffectType
from .rl03_development_node_type import RL03DevelopmentNodeType
from .roguelike_topic_display_item import RoguelikeTopicDisplayItem
from ..common import BaseStruct


class RL03Development(BaseStruct):
    buffId: str
    nodeType: RL03DevelopmentNodeType
    frontNodeId: list[str]
    nextNodeId: list[str]
    positionRow: int
    positionOrder: int
    tokenCost: int
    buffName: str
    buffIconId: str
    effectType: RL03DevelopmentEffectType
    rawDesc: list[str]
    buffDisplayInfo: list[RoguelikeTopicDisplayItem]
    groupId: str
    enrollId: str | None
