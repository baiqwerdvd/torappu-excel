from .shop_credit_unlock_item import ShopCreditUnlockItem
from ..common import BaseStruct


class ShopCreditUnlockGroup(BaseStruct):
    id: str
    index: str
    startDateTime: int
    charDict: list[ShopCreditUnlockItem]
