from .sandbox_v2_battle_rush_enemy_config import SandboxV2BattleRushEnemyConfig
from ..common import BaseStruct


class SandboxV2BattleRushEnemyGroupConfig(BaseStruct):
    enemyGroupKey: str
    enemy: list[SandboxV2BattleRushEnemyConfig]
    dynamicEnemy: list[str]
