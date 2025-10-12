from pydantic import BaseModel, ConfigDict

from .zone_record_data import ZoneRecordData
from .zone_record_unlock_data import ZoneRecordUnlockData


class ZoneRecordGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneId: str
    records: list[ZoneRecordData]
    unlockData: ZoneRecordUnlockData
