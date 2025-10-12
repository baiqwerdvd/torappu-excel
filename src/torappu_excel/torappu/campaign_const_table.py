from pydantic import BaseModel, ConfigDict


class CampaignConstTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    systemPreposedStage: str
    rotateStartTime: int
    rotatePreposedStage: str
    zoneUnlockStage: str
    firstRotateRegion: str
    sweepStartTime: int
