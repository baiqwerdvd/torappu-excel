from pydantic import BaseModel, ConfigDict


class FavorData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    favorPoint: int
    percent: int
    battlePhase: int
