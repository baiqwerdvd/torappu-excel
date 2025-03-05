from .item_bundle import ItemBundle
from ..common import BaseStruct


class MedalRewardGroupData(BaseStruct):
    groupId: str
    slotId: int
    itemList: list[ItemBundle]
