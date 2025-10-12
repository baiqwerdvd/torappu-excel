from pydantic import BaseModel, ConfigDict


class Act42SideZoneAdditionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneId: str
    unlockText: str
