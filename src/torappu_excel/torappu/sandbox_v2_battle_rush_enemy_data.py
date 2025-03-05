from .sandbox_v2_battle_rush_enemy_group_config import SandboxV2BattleRushEnemyGroupConfig
from .sandbox_v2_enemy_rush_type import SandboxV2EnemyRushType
from ..common import BaseStruct

from msgspec import field


class SandboxV2BattleRushEnemyData(BaseStruct):
    rushEnemyGroupConfigs: dict[SandboxV2EnemyRushType, list[SandboxV2BattleRushEnemyGroupConfig]]
    rushEnemyDbRef: list["SandboxV2BattleRushEnemyData.RushEnemyDBRef"]

    class RushEnemyDBRef(BaseStruct):
        id_: str = field(name="id")
        level: int
