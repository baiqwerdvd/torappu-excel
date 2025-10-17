from ..common import BaseStruct


class Act4funEndingInfo(BaseStruct):
    endingId: str
    endingAvg: str
    endingDesc: str | None
    stageId: str | None
    isGoodEnding: bool
