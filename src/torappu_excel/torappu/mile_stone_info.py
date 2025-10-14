from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class MileStoneInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    mileStoneId: str
    orderId: int
    tokenNum: int
    mileStoneType: "MileStoneInfo.GoodType"
    normalItem: ItemBundle
    IsBonus: int

    class GoodType(StrEnum):
        NORMAL = "NORMAL"
        SPECIAL = "SPECIAL"
