from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class MonthlyDailyBonusGroup(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    startTime: int
    endTime: int
    items: list[ItemBundle]
    imgId: str
    backId: str
