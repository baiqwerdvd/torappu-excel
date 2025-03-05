from .roguelike_event_type import RoguelikeEventType
from ..common import BaseStruct


class RoguelikeRollNodeData(BaseStruct):
    class RoguelikeRollNodeGroupData(BaseStruct):
        nodeType: RoguelikeEventType

    zoneId: str
    groups: dict[str, "RoguelikeRollNodeData.RoguelikeRollNodeGroupData"]
