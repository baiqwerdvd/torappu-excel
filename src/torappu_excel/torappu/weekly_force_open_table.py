from ..common import BaseStruct


class WeeklyForceOpenTable(BaseStruct):
    id: str
    startTime: int
    endTime: int
    forceOpenList: list[str]
