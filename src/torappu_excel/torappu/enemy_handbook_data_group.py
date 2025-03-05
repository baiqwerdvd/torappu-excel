from .enemy_handbook_data import EnemyHandBookData
from .enemy_handbook_level_info_data import EnemyHandbookLevelInfoData
from .enemy_handbook_race_data import EnemyHandbookRaceData
from ..common import BaseStruct


class EnemyHandBookDataGroup(BaseStruct):
    levelInfoList: list[EnemyHandbookLevelInfoData]
    enemyData: dict[str, EnemyHandBookData]
    raceData: dict[str, EnemyHandbookRaceData]
