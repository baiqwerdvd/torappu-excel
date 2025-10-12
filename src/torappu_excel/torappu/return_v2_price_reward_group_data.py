from pydantic import BaseModel, ConfigDict

from .return_v2_price_reward_data import ReturnV2PriceRewardData


class ReturnV2PriceRewardGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    startTime: int
    endTime: int
    contentList: list[ReturnV2PriceRewardData]
