from pydantic import BaseModel, ConfigDict


class PlayerBuildingHireBuff(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    speed: float
    point: dict[str, int]
    meeting: "PlayerBuildingHireBuff.Meeting"
    stack: "PlayerBuildingHireBuff.Stack"
    apCost: "PlayerBuildingHireBuff.ApCost"

    class ApCost(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        self: dict[str, int]

    class Meeting(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        speedUp: float | int

    class Stack(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        char: list["PlayerBuildingHireBuff.Stack.Char"]
        clueWeight: dict[str, int]

        class Char(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            refresh: int
