from pydantic import BaseModel, ConfigDict


class KVSwitchInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    isDefault: bool
    displayTime: int
    zoneId: str | None
