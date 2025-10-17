from .item_bundle import ItemBundle
from .sp_type import SpType
from ..common import BaseStruct


class SpData(BaseStruct):
    spType: SpType | int
    levelUpCost: list[ItemBundle] | None
    maxChargeTime: int
    spCost: int
    initSp: int
    increment: int | float
