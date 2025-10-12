from pydantic import BaseModel, ConfigDict

from .return_v2_item_data import ReturnV2ItemData


class ReturnV2PackageCheckInRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    startTime: int
    endTime: int
    getTime: int
    bindGPGoodId: str
    totalCheckInDay: int
    iconId: str
    rewardDict: dict[str, list[ReturnV2ItemData]]
