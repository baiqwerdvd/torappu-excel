from pydantic import BaseModel, ConfigDict, Field


class PlayerBuildingControlBuff(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    global_: "PlayerBuildingControlBuff.Global" = Field(alias="global")
    manufacture: "PlayerBuildingControlBuff.Manufacture"
    trading: "PlayerBuildingControlBuff.Trading"
    meeting: "PlayerBuildingControlBuff.Meeting"
    apCost: dict[str, int]
    point: dict[str, int]
    hire: "PlayerBuildingControlBuff.Hire"
    power: "PlayerBuildingControlBuff.Power"
    dormitory: "PlayerBuildingControlBuff.Dormitory"
    training: "PlayerBuildingControlBuff.Training"

    class Global(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        apCost: int
        roomCnt: dict[str, int]

    class Manufacture(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        speed: float | int
        sSpeed: float | int
        roomSpeed: dict[str, float | int]
        apCost: int

    class Trading(Manufacture):
        charSpeed: dict[str, float | int]
        charLimit: dict[str, int]
        roomLimit: dict[str, int]

    class Meeting(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        clue: float | int
        speedUp: float | int
        sSpeed: float | int
        weight: dict[str, float | int]
        apCost: int
        notOwned: float | int

    class Hire(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        spUp: "PlayerBuildingControlBuff.Hire.SpUp"
        apCost: int
        up: int

        class SpUp(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            base: float | int
            up: float | int

    class Power(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        apCost: int

    class Dormitory(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        recover: int
        tagRecover: dict[str, int]

    class Training(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        speed: float
