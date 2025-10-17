from .roguelike_event_type import RoguelikeEventType
from ..common import BaseStruct


class RoguelikeGameNodeSubTypeData(BaseStruct):
    eventType: RoguelikeEventType
    subTypeId: int
    iconId: str | None
    name: str | None
    description: str | None
