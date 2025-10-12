from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ReturnV2DailySupplyData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    startTime: int
    endTime: int
    rewardList: list[ItemBundle]
