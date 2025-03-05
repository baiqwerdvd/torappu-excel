from ..common import BaseStruct


class RushEnemyConfig(BaseStruct):
    enemyKey: str
    branchId: str
    count: int
    interval: float | int
