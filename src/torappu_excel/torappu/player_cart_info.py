from enum import StrEnum
from pydantic import BaseModel, ConfigDict


class PlayerCartInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class Cart(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        pass

    class CompInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        num: int
