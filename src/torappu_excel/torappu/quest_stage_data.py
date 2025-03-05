from ..common import BaseStruct


class QuestStageData(BaseStruct):
    stageId: str
    stageRank: int
    sortId: int
    isUrgentStage: bool
    isDragonStage: bool
