from .item_bundle import ItemBundle
from ..common import BaseStruct


class MonthlyDailyBonusGroup(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    items: list[ItemBundle]
    imgId: str
    backId: str
