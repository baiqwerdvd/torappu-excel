from .item_type import ItemType
from ..common import BaseStruct


class ArtMagazineLeafElementData(BaseStruct):
    id: str
    type: ItemType
    sub: int
    pos: list[float]
    scale: float
