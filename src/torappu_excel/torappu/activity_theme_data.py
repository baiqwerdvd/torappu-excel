from .activity_theme_type import ActivityThemeType
from ..common import BaseStruct

from msgspec import field


class ActivityThemeData(BaseStruct):
    id_: str = field(name="id")
    type_: ActivityThemeType = field(name="type")
    funcId: str
    endTs: int
    sortId: int
    itemId: str | None
    timeNodes: list["TimeNode"]
    startTs: int

    class TimeNode(BaseStruct):
        title: str
        ts: int
