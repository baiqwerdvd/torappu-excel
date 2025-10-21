from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActivitySwitchCheckinMainRewardShowData(BaseStruct):
    mainRewardPicId: str
    mainRewardName: str | None
    mainRewardCount: int
    hasTip: bool
    tipItemBundle: ItemBundle | None
