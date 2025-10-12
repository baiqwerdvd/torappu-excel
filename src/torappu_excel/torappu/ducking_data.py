from pydantic import BaseModel, ConfigDict, Field


class DuckingData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    bank: str
    volume: float
    fadeTime: float
    delay: float
    fadeStyleId: str | None = Field(default=None)
