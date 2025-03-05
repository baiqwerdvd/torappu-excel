from .item_bundle import ItemBundle
from ..common import BaseStruct

from msgspec import field


class EPGSGood(BaseStruct):
    goodId: str
    goodType: str
    startTime: int
    availCount: int
    item: ItemBundle
    price: int
    sortId: int
    endTime: int | None = field(default=None)
