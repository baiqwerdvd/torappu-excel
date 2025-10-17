from .item_type import ItemType
from .stage_drop_type import StageDropType
from ..common import BaseStruct


class WeightItemBundle(BaseStruct):
    id: str
    type: ItemType
    dropType: StageDropType
    count: int
    weight: int
