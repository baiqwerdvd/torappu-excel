from pydantic import BaseModel, ConfigDict


class SandboxV2ZoneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneId: str
    zoneName: str
    displayName: bool
    appellation: str | None
