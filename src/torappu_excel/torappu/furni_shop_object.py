from .furn_shop_display_place import FurnShopDisplayPlace
from ..common import BaseStruct

from msgspec import field


class FurniShopObject(BaseStruct):
    goodId: str
    furniId: str
    displayName: str
    shopDisplay: FurnShopDisplayPlace
    priceCoin: int
    priceDia: int
    discount: float | int
    originPriceCoin: int
    originPriceDia: int
    end: int
    count: int
    sequence: int
    begin: int | None = field(default=None)
