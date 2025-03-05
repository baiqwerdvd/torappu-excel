from .rush_enemy_config import RushEnemyConfig
from ..common import BaseStruct


class RushEnemyGroupConfig(BaseStruct):
    enemyGroupKey: str
    weight: int
    enemy: list[RushEnemyConfig]
    dynamicEnemy: list[str]
