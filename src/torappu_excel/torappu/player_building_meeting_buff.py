from pydantic import BaseModel, ConfigDict


class PlayerBuildingMeetingBuff(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    speed: float
    weight: dict[str, float | int]
    flag: dict[str, float | int]
    apCost: "PlayerBuildingMeetingBuff.ApCost"
    notOwned: float | int
    owned: float | int

    class ApCost(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        self: dict[str, int]
