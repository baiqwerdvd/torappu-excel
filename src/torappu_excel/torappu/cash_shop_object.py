from ..common import BaseStruct


class CashShopObject(BaseStruct):
    goodId: str
    slotId: int
    price: int
    diamondNum: int
    doubleCount: int
    plusNum: int
    desc: str
