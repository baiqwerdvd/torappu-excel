from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .sp_type import SpType


class SpData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    spType: SpType | int
    levelUpCost: list[ItemBundle] | None
    maxChargeTime: int
    spCost: int
    initSp: int
    increment: int | float
