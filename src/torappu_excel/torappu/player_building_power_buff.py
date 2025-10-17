from msgspec import field

from ..common import BaseStruct


class PlayerBuildingPowerBuff(BaseStruct):
    laborSpeed: float
    apCost: "PlayerBuildingPowerBuff.ApCost"
    global_: "PlayerBuildingPowerBuff.Global" = field(name="global")
    manufacture: "PlayerBuildingPowerBuff.Manufacture"

    class ApCost(BaseStruct):
        self_: dict[str, int] = field(name="self")

    class Global(BaseStruct):
        roomCnt: dict[str, int]

    class Manufacture(BaseStruct):
        charSpeed: dict[str, float | int]
