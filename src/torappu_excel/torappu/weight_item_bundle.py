from .item_type import ItemType
from .stage_drop_type import StageDropType
from ..common import BaseStruct

from msgspec import field


class WeightItemBundle(BaseStruct):
    id_: str = field(name="id")
    type_: ItemType = field(name="type")
    dropType: StageDropType
    count: int
    weight: int
