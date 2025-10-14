from pydantic import BaseModel, ConfigDict, Field


class PlayerBuildingPowerBuff(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    laborSpeed: float
    apCost: "PlayerBuildingPowerBuff.ApCost"
    global_: "PlayerBuildingPowerBuff.Global" = Field(alias="global")
    manufacture: "PlayerBuildingPowerBuff.Manufacture"

    class ApCost(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        self_: dict[str, int] = Field(alias="self")

    class Global(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        roomCnt: dict[str, int]

    class Manufacture(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        charSpeed: dict[str, float | int]
