from .climb_tower_level_drop_info import ClimbTowerLevelDropInfo
from .climb_tower_level_type import ClimbTowerLevelType
from ..common import BaseStruct


class ClimbTowerSingleLevelData(BaseStruct):
    id: str
    levelId: str
    towerId: str
    layerNum: int
    code: str
    name: str
    desc: str
    levelType: ClimbTowerLevelType
    loadingPicId: str
    dropInfo: ClimbTowerLevelDropInfo
