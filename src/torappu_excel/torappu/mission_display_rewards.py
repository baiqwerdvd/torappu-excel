from .item_type import ItemType
from ..common import BaseStruct


class MissionDisplayRewards(BaseStruct):
    type: ItemType
    id: str
    count: int
