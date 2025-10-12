from pydantic import BaseModel, ConfigDict


class GridPosition(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    row: int
    col: int
