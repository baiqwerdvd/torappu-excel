from .item_type import ItemType
from ..common import BaseStruct

from msgspec import field


class MissionDisplayRewards(BaseStruct):
    type_: ItemType = field(name="type")
    id_: str = field(name="id")
    count: int
