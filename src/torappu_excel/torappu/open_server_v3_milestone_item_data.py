from .item_bundle import ItemBundle
from ..common import BaseStruct


class OpenServerV3MilestoneItemData(BaseStruct):
    level: int
    reward: ItemBundle
    pointId: str
    pointCnt: int
    isBonus: bool
