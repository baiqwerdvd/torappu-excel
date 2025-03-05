from .roguelike_event_type import RoguelikeEventType
from ..common import BaseStruct


class RoguelikeGameNodeSubTypeData(BaseStruct):
    eventType: RoguelikeEventType
    subTypeId: int
    iconId: str
    name: str | None
    description: str
