from pydantic import BaseModel, ConfigDict

from .activity_theme_type import ActivityThemeType
from .common_avail_check import CommonAvailCheck


class ActivityThemeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: ActivityThemeType
    funcId: str
    endTs: int
    sortId: int
    itemId: str | None
    timeNodes: list["TimeNode"]
    picGroups: list["PicGroup"]
    startTs: int

    class TimeNode(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        title: str
        ts: int

    class PicGroup(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        sortIndex: int
        picId: str
        availCheck: CommonAvailCheck
