from .char_master_level_data import CharMasterLevelData
from .char_master_type import CharMasterType
from ..common import BaseStruct


class CharMasterBasicData(BaseStruct):
    charId: str
    masterId: str
    sortId: int
    masterType: CharMasterType
    levelList: list[CharMasterLevelData]
