from pydantic import BaseModel, ConfigDict

from .enemy_handbook_data import EnemyHandBookData
from .enemy_handbook_level_info_data import EnemyHandbookLevelInfoData
from .enemy_handbook_race_data import EnemyHandbookRaceData


class EnemyHandBookDataGroup(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    levelInfoList: list[EnemyHandbookLevelInfoData]
    enemyData: dict[str, EnemyHandBookData]
    raceData: dict[str, EnemyHandbookRaceData]
