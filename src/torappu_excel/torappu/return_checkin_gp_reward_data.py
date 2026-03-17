from .return_item_data import ReturnItemData
from ..common import BaseStruct


class ReturnCheckinGpRewardData(BaseStruct):
    groupId: str
    getTime: int
    bindGPGoodId: str
    totalCheckInDay: int
    iconId: str
    rewardDict: dict[str, list[ReturnItemData]]
