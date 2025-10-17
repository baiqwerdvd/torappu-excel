from ..common import BaseStruct


class SandboxStageData(BaseStruct):
    stageId: str
    levelId: str
    code: str
    name: str
    loadingPicId: str
    description: str
    actionCost: int
    powerCost: int
