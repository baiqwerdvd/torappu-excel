from pydantic import BaseModel, ConfigDict


class PlayerZone(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    completeTimes: int
