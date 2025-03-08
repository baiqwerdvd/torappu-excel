from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActMultiV3MilestoneData(BaseStruct):
    id: str
    level: int
    needPointCnt: int
    rewardItem: ItemBundle
    availTime: int
