from pydantic import BaseModel, ConfigDict


class TimelyDropTimeInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    startTs: int
    endTs: int
    stagePic: str | None
    dropPicId: str | None
    stageUnlock: str
    entranceDownPicId: str | None
    entranceUpPicId: str | None
    timelyGroupId: str
    weeklyPicId: str | None
    apSupplyOutOfDateDict: dict[str, int]
    isReplace: bool
