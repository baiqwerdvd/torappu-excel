from .item_type import ItemType
from ..common import BaseStruct

from msgspec import field


class ReturnV2ItemData(BaseStruct):
    type_: ItemType = field(name="type")
    id_: str = field(name="id")
    count: int
    sortId: int
