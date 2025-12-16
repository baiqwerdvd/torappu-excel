from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActivityCommonMilestoneData(BaseStruct):
    milestoneId: str
    milestoneLvl: int
    tokenNum: int
    rewardItem: ItemBundle
    availableTime: int
