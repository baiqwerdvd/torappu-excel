from enum import StrEnum

from .stage_diff_group import StageDiffGroup
from ..common import BaseStruct


class MainlineZoneData(BaseStruct):
    class ZoneReplayBtnType(StrEnum):
        NONE = "NONE"
        RECAP = "RECAP"
        REPLAY = "REPLAY"

    zoneId: str
    chapterId: str
    preposedZoneId: str | None
    zoneIndex: int
    startStageId: str
    endStageId: str
    mainlneBgName: str
    recapId: str
    recapPreStageId: str
    buttonName: str
    buttonStyle: "MainlineZoneData.ZoneReplayBtnType"
    spoilAlert: bool
    zoneOpenTime: int
    diffGroup: list[StageDiffGroup]
