from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from .stage_diff_group import StageDiffGroup


class MainlineZoneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
    mainlneBgName: str | None = Field(default=None)
