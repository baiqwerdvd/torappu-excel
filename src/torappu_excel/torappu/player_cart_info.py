from enum import StrEnum

from ..common import BaseStruct


class PlayerCartInfo(BaseStruct):
    battleCar: dict["PlayerCartInfo.CartAccessoryPos", str]
    exhibitionCar: dict["PlayerCartInfo.CartAccessoryPos", str | None]
    accessories: dict[str, "PlayerCartInfo.CompInfo"]

    class CartAccessoryPos(StrEnum):
        NONE = "NONE"
        ROOF = "ROOF"
        HEADSTOCK = "HEADSTOCK"
        TRUNK_01 = "TRUNK_01"
        TRUNK_02 = "TRUNK_02"
        CAR_OS_01 = "CAR_OS_01"
        CAR_OS_02 = "CAR_OS_02"

    class Cart(BaseStruct):
        pass

    class CompInfo(BaseStruct):
        id: str
        num: int
