from .shop_credit_unlock_item import ShopCreditUnlockItem
from ..common import BaseStruct

from msgspec import field


class ShopCreditUnlockGroup(BaseStruct):
    id_: str = field(name="id")
    index: str
    startDateTime: int
    charDict: list[ShopCreditUnlockItem]
