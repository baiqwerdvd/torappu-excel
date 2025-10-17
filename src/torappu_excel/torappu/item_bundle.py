from .item_type import ItemType
from ..common import BaseStruct


class ItemBundle(BaseStruct):
    id: str
    count: int
    type: ItemType
