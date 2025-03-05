from .return_v2_checkin_reward_item_data import ReturnV2CheckInRewardItemData
from ..common import BaseStruct


class ReturnV2CheckInRewardData(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    rewardList: list[ReturnV2CheckInRewardItemData]
