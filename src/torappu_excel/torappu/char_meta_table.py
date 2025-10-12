from pydantic import BaseModel, ConfigDict

from .char_master_basic_data import CharMasterBasicData
from .sp_char_mission_data import SpCharMissionData


class CharMetaTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    spCharGroups: dict[str, list[str]]
    spCharMissions: dict[str, dict[str, SpCharMissionData]]
    spCharVoucherSkinTime: dict[str, int]
    charIdMasterListMap: dict[str, list[str]]
    charMasterDataMap: dict[str, CharMasterBasicData]
