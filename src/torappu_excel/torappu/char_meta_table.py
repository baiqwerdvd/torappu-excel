from .sp_char_mission_data import SpCharMissionData
from ..common import BaseStruct


class CharMetaTable(BaseStruct):
    spCharGroups: dict[str, list[str]]
    spCharMissions: dict[str, dict[str, "SpCharMissionData"]]
    spCharVoucherSkinTime: dict[str, int]
