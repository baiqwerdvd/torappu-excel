from ..common import BaseStruct


class PlayerBuildingManufactureBuff(BaseStruct):
    apCost: "PlayerBuildingManufactureBuff.ApCost"
    speed: float | int
    sSpeed: float | int
    capacity: int
    maxSpeed: int
    tSpeed: dict[str, float | int]
    cSpeed: float | int
    capFrom: dict[str, int]
    point: dict[str, int]
    flag: dict[str, int]
    skillExtend: dict[str, list[str]]

    class ApCost(BaseStruct):
        self: dict[str, int]
        all: int
