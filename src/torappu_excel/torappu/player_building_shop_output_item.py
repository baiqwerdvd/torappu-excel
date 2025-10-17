from .item_type import ItemType
from ..common import BaseStruct


class PlayerBuildingShopOutputItem(BaseStruct):
    type: ItemType
    count: int
