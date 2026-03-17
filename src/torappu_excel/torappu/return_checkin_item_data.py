from .item_bundle import ItemBundle
from ..common import BaseStruct


class ReturnCheckinItemData(BaseStruct):
    order: int
    isKeyItem: bool
    rewardList: list[ItemBundle]
