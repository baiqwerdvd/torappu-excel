from pydantic import BaseModel, ConfigDict

from torappu_excel.common import CustomIntEnum

from .item_bundle import ItemBundle


class MileStoneInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class GoodType(CustomIntEnum):
        NORMAL = "NORMAL", 0
        SPECIAL = "SPECIAL", 1

    mileStoneId: str
    orderId: int
    tokenNum: int
    mileStoneType: "MileStoneInfo.GoodType"
    normalItem: ItemBundle
    IsBonus: int
