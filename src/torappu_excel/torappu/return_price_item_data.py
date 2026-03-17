from .return_item_data import ReturnItemData
from ..common import BaseStruct


class ReturnPriceItemData(BaseStruct):
    contentId: str
    sortId: int
    pointRequire: int
    desc: str
    displayReward: ReturnItemData
    rewardList: list[ReturnItemData]
