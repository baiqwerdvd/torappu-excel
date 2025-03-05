from .roguelike_topic_dev_node_type import RoguelikeTopicDevNodeType
from .roguelike_topic_display_item import RoguelikeTopicDisplayItem
from ..common import BaseStruct


class RoguelikeTopicDev(BaseStruct):
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
