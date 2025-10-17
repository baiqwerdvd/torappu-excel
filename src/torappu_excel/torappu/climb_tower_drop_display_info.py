from .item_type import ItemType
from ..common import BaseStruct


class ClimbTowerDropDisplayInfo(BaseStruct):
    itemId: str
    type: ItemType
    maxCount: int
    minCount: int
