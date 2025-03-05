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
    canPreview: bool
    hasAdditionalPanel: bool | None = field(default=None)
