from pydantic import BaseModel, ConfigDict


class PlayerEvents(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    building: int
    status: int
