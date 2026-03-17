from .item_type import ItemType
from ..common import BaseStruct


class ReturnItemData(BaseStruct):
    id: str
    count: int
    type: ItemType
    sortId: int
