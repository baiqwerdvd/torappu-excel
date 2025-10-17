from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActivitySwitchCheckinRewardItemShowData(BaseStruct):
    itemBundle: ItemBundle
    isMainReward: bool
