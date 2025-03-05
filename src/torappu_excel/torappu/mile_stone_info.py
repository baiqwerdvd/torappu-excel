from .item_bundle import ItemBundle
from ..common import BaseStruct, CustomIntEnum


class MileStoneInfo(BaseStruct):
    class GoodType(CustomIntEnum):
        NORMAL = "NORMAL", 0
        SPECIAL = "SPECIAL", 1

    mileStoneId: str
    orderId: int
    tokenNum: int
    mileStoneType: "MileStoneInfo.GoodType"
    normalItem: ItemBundle
    IsBonus: int
