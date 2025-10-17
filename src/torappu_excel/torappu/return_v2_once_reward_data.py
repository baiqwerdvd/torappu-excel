from .return_v2_item_data import ReturnV2ItemData
from ..common import BaseStruct


class ReturnV2OnceRewardData(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    rewardList: list[ReturnV2ItemData]
