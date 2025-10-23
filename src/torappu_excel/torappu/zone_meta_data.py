from msgspec import field

from .zone_record_mission_data import ZoneRecordMissionData
from ..common import BaseStruct


class ZoneMetaData(BaseStruct):
    zoneRecordMissionData: dict[str, ZoneRecordMissionData] = field(name="ZoneRecordMissionData")
