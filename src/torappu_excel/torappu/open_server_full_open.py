from pydantic import BaseModel, ConfigDict


class OpenServerFullOpen(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    isAvailable: bool
    startTs: int
    today: bool
    remain: int
