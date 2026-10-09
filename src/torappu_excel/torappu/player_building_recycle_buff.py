from msgspec import field

from ..common import BaseStruct


class PlayerBuildingRecycleBuff(BaseStruct):
    apCost: "PlayerBuildingRecycleBuff.ApCost"
    boostSpeed: float | int
    speed: float | int

    class ApCost(BaseStruct):
        all: int
        self_: dict[str, int] = field(name="self")
