from pydantic import BaseModel, ConfigDict


class OpenServerCheckIn(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    isAvailable: bool
    history: list[bool]
