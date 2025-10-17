from .item_bundle import ItemBundle
from ..common import BaseStruct


class SandboxV2MonthRushData(BaseStruct):
    monthlyRushId: str
    startTime: int
    endTime: int
    isLast: bool
    sortId: int
    rushGroupKey: str
    monthlyRushName: str
    monthlyRushDes: str
    weatherId: str
    nodeId: str
    conditionGroup: str
    conditionDesc: str
    rewardItemList: list[ItemBundle]
