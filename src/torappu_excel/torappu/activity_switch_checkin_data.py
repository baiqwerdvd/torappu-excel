from .activity_switch_checkin_const_data import ActivitySwitchCheckinConstData
from .activity_switch_checkin_reward_show_data import ActivitySwitchCheckinRewardShowData
from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActivitySwitchCheckinData(BaseStruct):
    constData: ActivitySwitchCheckinConstData
    rewards: dict[str, list[ItemBundle]]
    rewardShowDatas: dict[str, ActivitySwitchCheckinRewardShowData]
    apSupplyOutOfDateDict: dict[str, int]
    sortIdDict: dict[str, int]
    rewardsTitle: dict[str, str] | None = None
