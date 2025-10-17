from enum import StrEnum

from .item_bundle import ItemBundle
from ..common import BaseStruct


class MileStoneInfo(BaseStruct):
    mileStoneId: str
    orderId: int
    tokenNum: int
    mileStoneType: "MileStoneInfo.GoodType"
    normalItem: ItemBundle
    IsBonus: int

    class GoodType(StrEnum):
        NORMAL = "NORMAL"
        SPECIAL = "SPECIAL"
