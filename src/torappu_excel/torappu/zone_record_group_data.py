from .zone_record_data import ZoneRecordData
from .zone_record_unlock_data import ZoneRecordUnlockData
from ..common import BaseStruct


class ZoneRecordGroupData(BaseStruct):
    zoneId: str
    records: list[ZoneRecordData]
    unlockData: ZoneRecordUnlockData
