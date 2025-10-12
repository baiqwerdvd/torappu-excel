from pydantic import BaseModel, ConfigDict, Field


class BGMBank(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    name: str
    intro: str | None
    loop: str | None
    volume: float
    crossfade: float
    delay: float
    fadeStyleId: str | None = Field(default=None)
