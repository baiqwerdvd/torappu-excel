from .item_bundle import ItemBundle
from .shop_currency_unit import ShopCurrencyUnit
from .special_item_info import SpecialItemInfo
from ..common import BaseStruct

from msgspec import field


class GPShopNormalGPItem(BaseStruct):
    goodId: str
    giftPackageId: str
    priority: int
    displayName: str
    currencyUnit: ShopCurrencyUnit
    availCount: int
    price: int
    originPrice: int
    discount: float | int
    items: list[ItemBundle]
    specialItemInfos: dict[str, SpecialItemInfo]
    startDateTime: int = field(default=0)
    endDateTime: int = field(default=0)
    groupId: str | None = field(default=None)
    buyCount: int | None = field(default=None)
