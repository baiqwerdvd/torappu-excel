from ..common import BaseStruct


class SkinShopItemViewModel(BaseStruct):
    goodId: str
    skinName: str
    skinId: str
    charId: str
    currencyUnit: str
    originPrice: int
    price: int
    discount: float | int
    desc1: str | None
    desc2: str | None
    startDateTime: int
    endDateTime: int
    slotId: int
    isRedeem: bool
