from ..common import BaseStruct


class SandboxV2StageData(BaseStruct):
    stageId: str
    levelId: str
    code: str
    name: str
    description: str
    actionCost: int
    actionCostEnemyRush: int
