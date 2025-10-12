from pydantic import BaseModel, ConfigDict


class Vector2(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    x: float
    y: float
