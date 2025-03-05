from .item_bundle import ItemBundle
from ..common import BaseStruct


class QCProgressGoodItem(BaseStruct):
    order: int
    price: int
    displayName: str
    item: ItemBundle
