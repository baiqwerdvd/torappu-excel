from .char_master_basic_data import CharMasterBasicData
from .sp_char_mission_data import SpCharMissionData
from ..common import BaseStruct


class CharMetaTable(BaseStruct):
    spCharGroups: dict[str, list[str]]
    spCharMissions: dict[str, dict[str, SpCharMissionData]]
    spCharVoucherSkinTime: dict[str, int]
    charIdMasterListMap: dict[str, list[str]]
    charMasterDataMap: dict[str, CharMasterBasicData]
