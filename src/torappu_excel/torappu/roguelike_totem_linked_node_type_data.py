from .roguelike_event_type import RoguelikeEventType
from .roguelike_totem_blur_node_type import RoguelikeTotemBlurNodeType
from ..common import BaseStruct


class RoguelikeTotemLinkedNodeTypeData(BaseStruct):
    effectiveNodeTypes: list[RoguelikeEventType]
    blurNodeTypes: list[RoguelikeTotemBlurNodeType]
