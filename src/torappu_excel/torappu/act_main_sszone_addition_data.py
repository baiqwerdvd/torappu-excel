from pydantic import BaseModel, ConfigDict


class ActMainSSZoneAdditionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    unlockTip: str
    unlockTipAfterRetro: str
