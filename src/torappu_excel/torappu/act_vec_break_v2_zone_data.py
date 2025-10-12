from pydantic import BaseModel, ConfigDict


class ActVecBreakV2ZoneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneId: str
    stageLockHint: str | None
