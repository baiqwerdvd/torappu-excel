from .item_type import ItemType
from ..common import BaseStruct

from msgspec import field


class ItemBundle(BaseStruct):
    id_: str = field(name="id")
    count: int
    type_: ItemType = field(name="type")
