from .roguelike_event_type import RoguelikeEventType
from .roguelike_move_scrap_range_type import RoguelikeMoveScrapRangeType
from ..common import BaseStruct


class RoguelikeScrapMoveData(BaseStruct):
    count: int
    range: str | None
    rangeType: RoguelikeMoveScrapRangeType
    node: list[str]
    step: int
    isRandomMove: bool
    nodeChangeTargetType: RoguelikeEventType
    scrapId: str
    scrapDesc: str
    sellPrice: int
