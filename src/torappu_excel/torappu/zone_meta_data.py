from .zone_record_mission_data import ZoneRecordMissionData
from ..common import BaseStruct


class ZoneMetaData(BaseStruct):
    ZoneRecordMissionData: dict[str, ZoneRecordMissionData]
