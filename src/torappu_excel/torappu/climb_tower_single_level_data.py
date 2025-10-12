from pydantic import BaseModel, ConfigDict

from .climb_tower_level_drop_info import ClimbTowerLevelDropInfo
from .climb_tower_level_type import ClimbTowerLevelType


class ClimbTowerSingleLevelData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
