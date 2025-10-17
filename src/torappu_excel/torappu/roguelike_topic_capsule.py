from .roguelike_event_type import RoguelikeEventType
from ..common import BaseStruct


class RoguelikeTopicCapsule(BaseStruct):
    itemId: str
    maskType: RoguelikeEventType
    innerColor: str
