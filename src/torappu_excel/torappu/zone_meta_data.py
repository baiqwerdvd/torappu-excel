from pydantic import BaseModel, ConfigDict

from .zone_record_mission_data import ZoneRecordMissionData


class ZoneMetaData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    ZoneRecordMissionData: dict[str, ZoneRecordMissionData]
