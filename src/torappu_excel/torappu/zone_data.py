from .zone_type import ZoneType
from ..common import BaseStruct

from msgspec import field


class ZoneData(BaseStruct):
    zoneID: str
    zoneIndex: int
    type_: ZoneType = field(name="type")
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
    hasAdditionalPanel: bool | None = field(default=None)
