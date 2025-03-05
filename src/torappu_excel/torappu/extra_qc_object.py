from .extra_shop_group_type import ExtraShopGroupType
from .item_bundle import ItemBundle
from ..common import BaseStruct


class ExtraQCObject(BaseStruct):
    goodId: str
    item: ItemBundle
    displayName: str
    slotId: int
    originPrice: int
    price: int
    availCount: int
    discount: float | int
    goodEndTime: int
    shopType: ExtraShopGroupType
    newFlagTimeStamp: int
