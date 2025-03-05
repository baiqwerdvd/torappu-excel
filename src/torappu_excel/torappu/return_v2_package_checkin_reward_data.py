from .return_v2_item_data import ReturnV2ItemData
from ..common import BaseStruct


class ReturnV2PackageCheckInRewardData(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    getTime: int
    bindGPGoodId: str
    totalCheckInDay: int
    iconId: str
    rewardDict: dict[str, list[ReturnV2ItemData]]
