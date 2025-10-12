from pydantic import BaseModel, ConfigDict, Field

from .zone_type import ZoneType


class ZoneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneID: str
    zoneIndex: int
    type: ZoneType
    zoneNameFirst: str | None
    zoneNameSecond: str | None
    zoneNameTitleCurrent: str | None
    zoneNameTitleUnCurrent: str | None
    zoneNameTitleEx: str | None
    zoneNameThird: str | None
    lockedText: str | None
    antiSpoilerId: str | None
    canPreview: bool
    sixStarMilestoneGroupId: str | None
    bindMainlineZoneId: str | None
    bindMainlineRetroZoneId: str | None
    hasAdditionalPanel: bool | None = Field(default=None)
