from .item_bundle import ItemBundle
from ..common import BaseStruct


class ReturnV2DailySupplyData(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    rewardList: list[ItemBundle]
