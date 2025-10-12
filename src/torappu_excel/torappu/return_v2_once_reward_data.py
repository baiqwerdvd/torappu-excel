from pydantic import BaseModel, ConfigDict

from .return_v2_item_data import ReturnV2ItemData


class ReturnV2OnceRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    startTime: int
    endTime: int
    rewardList: list[ReturnV2ItemData]
