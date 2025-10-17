from .item_bundle import ItemBundle
from ..common import BaseStruct


class DefaultShopData(BaseStruct):
    goodId: str
    slotId: int
    price: int
    availCount: int
    overrideName: str
    item: ItemBundle
