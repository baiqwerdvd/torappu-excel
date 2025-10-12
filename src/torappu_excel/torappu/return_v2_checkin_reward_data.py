from pydantic import BaseModel, ConfigDict

from .return_v2_checkin_reward_item_data import ReturnV2CheckInRewardItemData


class ReturnV2CheckInRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    startTime: int
    endTime: int
    rewardList: list[ReturnV2CheckInRewardItemData]
