from .newbie_checkin_package_reward_data import NewbieCheckInPackageRewardData
from ..common import BaseStruct


class NewbieCheckInPackageData(BaseStruct):
    groupId: str
    startTime: int
    endTime: int
    bindGPGoodId: str
    checkInDuration: int
    totalCheckInDay: int
    iconId: str
    checkInRewardDict: dict[str, list[NewbieCheckInPackageRewardData]]
