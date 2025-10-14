from pydantic import BaseModel, ConfigDict


class PlayerBuildingTradingNext(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    order: int
    processPoint: float
    speed: float
    maxPoint: int
