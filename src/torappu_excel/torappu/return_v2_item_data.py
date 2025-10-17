from .item_type import ItemType
from ..common import BaseStruct


class ReturnV2ItemData(BaseStruct):
    type: ItemType
    id: str
    count: int
    sortId: int
