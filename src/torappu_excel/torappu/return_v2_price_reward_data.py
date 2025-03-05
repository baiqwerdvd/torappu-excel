from .return_v2_item_data import ReturnV2ItemData
from ..common import BaseStruct


class ReturnV2PriceRewardData(BaseStruct):
    contentId: str
    sortId: int
    pointRequire: int
    desc: str
    iconId: str
    topIconId: str
    rewardList: list[ReturnV2ItemData]
