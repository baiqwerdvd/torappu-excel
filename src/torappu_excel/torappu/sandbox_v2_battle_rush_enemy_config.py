from ..common import BaseStruct


class SandboxV2BattleRushEnemyConfig(BaseStruct):
    enemyKey: str
    branchId: str
    count: int
    interval: float
    preDelay: float
