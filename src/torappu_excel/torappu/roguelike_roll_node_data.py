from .roguelike_event_type import RoguelikeEventType
from ..common import BaseStruct


class RoguelikeRollNodeData(BaseStruct):
    zoneId: str
    groups: dict[str, "RoguelikeRollNodeData.RoguelikeRollNodeGroupData"]

    class RoguelikeRollNodeGroupData(BaseStruct):
        nodeType: RoguelikeEventType
