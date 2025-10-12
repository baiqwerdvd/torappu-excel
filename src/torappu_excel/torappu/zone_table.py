from pydantic import BaseModel, ConfigDict

from .mainline_zone_data import MainlineZoneData
from .weekly_zone_data import WeeklyZoneData
from .zone_data import ZoneData
from .zone_meta_data import ZoneMetaData
from .zone_record_group_data import ZoneRecordGroupData
from .zone_valid_info import ZoneValidInfo


class ZoneTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zones: dict[str, ZoneData]
    weeklyAdditionInfo: dict[str, WeeklyZoneData]
    zoneValidInfo: dict[str, ZoneValidInfo]
    mainlineAdditionInfo: dict[str, MainlineZoneData]
    zoneRecordGroupedData: dict[str, ZoneRecordGroupData]
    zoneRecordRewardData: dict[str, list[str]]
    mainlineZoneIdList: list[str]
    zoneMetaData: ZoneMetaData
