from enum import StrEnum

from ..common import BaseStruct

from msgspec import field


class CartComponents(BaseStruct):
    class CartAccessoryType(StrEnum):
        NONE = "NONE"
        ROOF = "ROOF"
        HEADSTOCK = "HEADSTOCK"
        TRUNK = "TRUNK"
        CAR_OS = "CAR_OS"

    class CartAccessoryPos(StrEnum):
        NONE = "NONE"
        ROOF = "ROOF"
        HEADSTOCK = "HEADSTOCK"
        TRUNK_01 = "TRUNK_01"
        TRUNK_02 = "TRUNK_02"
        CAR_OS_01 = "CAR_OS_01"
        CAR_OS_02 = "CAR_OS_02"

    compId: str
    sortId: int
    type_: "CartComponents.CartAccessoryType" = field(name="type")
    posList: list["CartComponents.CartAccessoryPos"]
    posIdDict: dict["CartComponents.CartAccessoryPos", list[str]]
    name: str
    icon: str
    showScores: int
    itemUsage: str
    itemDesc: str
    itemObtain: str
    rarity: int
    detailDesc: str
    price: int
    specialObtain: str
    obtainInRandom: bool
    additiveColor: str | None
