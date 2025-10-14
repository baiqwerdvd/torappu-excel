from pydantic import BaseModel, ConfigDict


class PlayerBuildingManufactureBuff(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class ApCost(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        self: dict[str, int]
        all: int
