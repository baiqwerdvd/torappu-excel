from pydantic import BaseModel, ConfigDict

from .activity_switch_checkin_main_reward_show_data import ActivitySwitchCheckinMainRewardShowData
from .activity_switch_checkin_reward_item_show_data import ActivitySwitchCheckinRewardItemShowData


class ActivitySwitchCheckinRewardShowData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    checkinId: str
    rewardsTitle: str
    rewardShowItemDatas: list[ActivitySwitchCheckinRewardItemShowData]
    mainRewardShowData: ActivitySwitchCheckinMainRewardShowData
