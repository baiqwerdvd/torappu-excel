from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class SandboxV2MonthRushData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    monthlyRushId: str
    startTime: int
    endTime: int
    isLast: bool
    sortId: int
    rushGroupKey: str
    monthlyRushName: str
    monthlyRushDes: str
    weatherId: str
    nodeId: str
    conditionGroup: str
    conditionDesc: str
    rewardItemList: list[ItemBundle]
