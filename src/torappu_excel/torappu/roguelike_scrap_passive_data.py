from .roguelike_event_type import RoguelikeEventType
from ..common import BaseStruct


class RoguelikeScrapPassiveData(BaseStruct):
    node: RoguelikeEventType | int
    buffStack: int
    scrapId: str
    scrapDesc: str
    sellPrice: int
