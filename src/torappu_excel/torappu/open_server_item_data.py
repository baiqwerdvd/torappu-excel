from .item_type import ItemType
from ..common import BaseStruct


class OpenServerItemData(BaseStruct):
    itemId: str
    itemType: ItemType
    count: int
    name: str | None
