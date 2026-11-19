from .item_bundle import ItemBundle
from ..common import BaseStruct


class OpenServerV3CheckInItemData(BaseStruct):
    order: int
    isKeyItem: bool
    rewardList: list[ItemBundle]
