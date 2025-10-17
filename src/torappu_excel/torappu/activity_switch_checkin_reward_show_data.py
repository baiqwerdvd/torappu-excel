from .activity_switch_checkin_main_reward_show_data import ActivitySwitchCheckinMainRewardShowData
from .activity_switch_checkin_reward_item_show_data import ActivitySwitchCheckinRewardItemShowData
from ..common import BaseStruct


class ActivitySwitchCheckinRewardShowData(BaseStruct):
    checkinId: str
    rewardsTitle: str
    rewardShowItemDatas: list[ActivitySwitchCheckinRewardItemShowData]
    mainRewardShowData: ActivitySwitchCheckinMainRewardShowData
