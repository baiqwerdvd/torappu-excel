from ..common import BaseStruct


class TimelyDropTimeInfo(BaseStruct):
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
