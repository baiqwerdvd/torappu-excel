from .item_type import ItemType
from ..common import BaseStruct

from msgspec import field


class ClimbTowerDropDisplayInfo(BaseStruct):
    itemId: str
    type_: ItemType = field(name="type")
    maxCount: int
    minCount: int
