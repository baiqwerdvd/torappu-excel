from pydantic import BaseModel, ConfigDict

from .rl02_development_effect_type import RL02DevelopmentEffectType
from .rl02_development_node_type import RL02DevelopmentNodeType
from .roguelike_topic_display_item import RoguelikeTopicDisplayItem


class RL02Development(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
