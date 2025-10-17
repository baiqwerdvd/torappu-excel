from enum import StrEnum

from msgspec import field

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
    gameMusicId: str
    recapId: str
    recapPreStageId: str
    buttonName: str
    buttonStyle: "MainlineZoneData.ZoneReplayBtnType"
    spoilAlert: bool
    zoneOpenTime: int
    diffGroup: list[StageDiffGroup]
    mainlneBgName: str | None = field(default=None)
