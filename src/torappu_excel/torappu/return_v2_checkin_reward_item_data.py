from .item_bundle import ItemBundle
from ..common import BaseStruct


class ReturnV2CheckInRewardItemData(BaseStruct):
    sortId: int
    isImportant: bool
    rewardList: list[ItemBundle]
