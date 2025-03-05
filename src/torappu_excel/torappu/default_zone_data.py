from ..common import BaseStruct


class DefaultZoneData(BaseStruct):
    zoneId: str
    zoneIndex: str
    zoneName: str
    zoneDesc: str
    itemDropList: list[str]
