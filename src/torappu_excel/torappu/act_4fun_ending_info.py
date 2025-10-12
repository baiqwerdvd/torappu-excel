from pydantic import BaseModel, ConfigDict


class Act4funEndingInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    endingId: str
    endingAvg: str
    endingDesc: str | None
    stageId: str | None
    isGoodEnding: bool
