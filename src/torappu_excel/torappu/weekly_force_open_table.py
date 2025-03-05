from ..common import BaseStruct

from msgspec import field


class WeeklyForceOpenTable(BaseStruct):
    id_: str = field(name="id")
    startTime: int
    endTime: int
    forceOpenList: list[str]
