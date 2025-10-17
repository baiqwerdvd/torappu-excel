from .player_zone_record_mission_process_data import PlayerZoneRecordMissionProcessData
from ..common import BaseStruct


class PlayerZoneRecordMissionData(BaseStruct):
    state: int
    process: PlayerZoneRecordMissionProcessData
