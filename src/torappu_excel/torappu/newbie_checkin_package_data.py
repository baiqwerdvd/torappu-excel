from pydantic import BaseModel, ConfigDict

from .newbie_checkin_package_reward_data import NewbieCheckInPackageRewardData


class NewbieCheckInPackageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    startTime: int
    endTime: int
    bindGPGoodId: str
    checkInDuration: int
    totalCheckInDay: int
    iconId: str
    checkInRewardDict: dict[str, list[NewbieCheckInPackageRewardData]]
