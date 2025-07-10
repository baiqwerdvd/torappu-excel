from .activity_theme_type import ActivityThemeType
from .common_avail_check import CommonAvailCheck
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
    picGroups: list["PicGroup"]
    startTs: int

    class TimeNode(BaseStruct):
        title: str
        ts: int

    class PicGroup(BaseStruct):
        sortIndex: int
        picId: str
        availCheck: CommonAvailCheck
