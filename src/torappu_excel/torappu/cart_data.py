from pydantic import BaseModel, ConfigDict

from .cart_components import CartComponents
from .rune_table import RuneTable


class CartData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    carDict: dict[str, CartComponents]
    runeDataDict: dict[str, RuneTable.PackedRuneData]
    cartStages: list[str]
    constData: "CartData.CartConstData"

    class CartConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        carItemUnlockStageId: str
        carItemUnlockDesc: str
        spLevelUnlockItemCnt: int
        mileStoneBaseInterval: int
        spStageIds: list[str]
        carFrameDefaultColor: str
