from pydantic import BaseModel, ConfigDict


class PlayerBuildingLabor(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buffSpeed: float
    value: int
    maxValue: int
    lastUpdateTime: int
    processPoint: float
