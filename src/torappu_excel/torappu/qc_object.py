from msgspec import field

from .item_bundle import ItemBundle
from .shop_qc_good_type import ShopQCGoodType
from ..common import BaseStruct


class QCObject(BaseStruct):
    goodId: str
    item: ItemBundle | None
    progressGoodId: str | None
    displayName: str | None
    originPrice: int
    price: int
    availCount: int
    discount: float | int
    priority: int
    number: int
    goodStartTime: int
    goodEndTime: int
    goodType: ShopQCGoodType
    slotId: int | None = field(default=None)
