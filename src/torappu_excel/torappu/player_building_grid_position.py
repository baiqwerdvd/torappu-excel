from pydantic import BaseModel, ConfigDict


class PlayerBuildingGridPosition(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    x: int
    y: int
    dir: int | None = None
