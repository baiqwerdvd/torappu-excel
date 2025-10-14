from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class CartComponents(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    compId: str
    sortId: int
    type: "CartComponents.CartAccessoryType"
    posList: "list[CartComponents.CartAccessoryPos]"
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
