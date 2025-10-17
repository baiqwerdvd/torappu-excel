from ..common import BaseStruct


class ActivityEnemyDuelPoolData(BaseStruct):
    enemyId: str
    poolNormal: float
    poolSmallEnemy: float
    poolBoss: float
    poolMusic: float
    poolNoSurpriseEnemy: float
