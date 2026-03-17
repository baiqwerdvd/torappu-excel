from .return_item_data import ReturnItemData
from ..common import BaseStruct


class ReturnOnceRewardData(BaseStruct):
    groupId: str
    rewardList: list[ReturnItemData]
