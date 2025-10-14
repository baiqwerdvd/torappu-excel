from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .player_mainline_explore import PlayerMainlineExplore
from .player_mission_archive import PlayerMissionArchive
from .player_zone_record_mission_data import PlayerZoneRecordMissionData


class PlayerMainlineRecord(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    record: dict[str, int]
    cache: list[ItemBundle]
    version: int
    additionalMission: dict[str, PlayerZoneRecordMissionData]
    charVoiceRecord: dict[str, PlayerMissionArchive]
    explore: PlayerMainlineExplore
