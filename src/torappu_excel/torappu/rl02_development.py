from .rl02_development_effect_type import RL02DevelopmentEffectType
from .rl02_development_node_type import RL02DevelopmentNodeType
from .roguelike_topic_display_item import RoguelikeTopicDisplayItem
from ..common import BaseStruct


class RL02Development(BaseStruct):
    buffId: str
    nodeType: RL02DevelopmentNodeType
    frontNodeId: list[str]
    nextNodeId: list[str]
    positionP: int
    positionR: int
    tokenCost: int
    buffName: str
    buffIconId: str
    effectType: RL02DevelopmentEffectType
    rawDesc: str
    buffDisplayInfo: list[RoguelikeTopicDisplayItem]
    enrollId: str | None
