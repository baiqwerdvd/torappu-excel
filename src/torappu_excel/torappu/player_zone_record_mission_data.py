from pydantic import BaseModel, ConfigDict

from .player_zone_record_mission_process_data import PlayerZoneRecordMissionProcessData


class PlayerZoneRecordMissionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    state: int
    process: PlayerZoneRecordMissionProcessData
