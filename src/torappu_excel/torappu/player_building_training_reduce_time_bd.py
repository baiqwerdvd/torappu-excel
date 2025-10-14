from pydantic import BaseModel, ConfigDict


class PlayerBuildingTrainingReduceTimeBd(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    fulltime: bool
    activated: bool
    cnt: int
    reset: bool
