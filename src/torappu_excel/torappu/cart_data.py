from .cart_components import CartComponents
from .rune_table import RuneTable
from ..common import BaseStruct


class CartData(BaseStruct):
    carDict: dict[str, CartComponents]
    runeDataDict: dict[str, RuneTable.PackedRuneData]
    cartStages: list[str]
    constData: "CartData.CartConstData"

    class CartConstData(BaseStruct):
        carItemUnlockStageId: str
        carItemUnlockDesc: str
        spLevelUnlockItemCnt: int
        mileStoneBaseInterval: int
        spStageIds: list[str]
        carFrameDefaultColor: str
