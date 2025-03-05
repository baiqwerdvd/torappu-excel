from .activity_switch_checkin_const_data import ActivitySwitchCheckinConstData
from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActivitySwitchCheckinData(BaseStruct):
    constData: ActivitySwitchCheckinConstData
    rewards: dict[str, list[ItemBundle]]
    apSupplyOutOfDateDict: dict[str, int]
    rewardsTitle: dict[str, str]
    sortIdDict: dict[str, int]
