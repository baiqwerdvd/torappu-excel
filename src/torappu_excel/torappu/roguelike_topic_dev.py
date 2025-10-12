from pydantic import BaseModel, ConfigDict

from .roguelike_topic_dev_node_type import RoguelikeTopicDevNodeType
from .roguelike_topic_display_item import RoguelikeTopicDisplayItem


class RoguelikeTopicDev(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buffId: str
    sortId: int
    nodeType: RoguelikeTopicDevNodeType
    nextNodeId: list[str]
    frontNodeId: list[str]
    tokenCost: int
    buffName: str
    buffIconId: str
    buffTypeName: str
    buffDisplayInfo: list[RoguelikeTopicDisplayItem]
