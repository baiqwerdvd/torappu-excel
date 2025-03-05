from ..common import BaseStruct


class ApProtectZoneInfo(BaseStruct):
    zoneId: str
    timeRanges: list["ApProtectZoneInfo.TimeRange"]

    class TimeRange(BaseStruct):
        startTs: int
        endTs: int
