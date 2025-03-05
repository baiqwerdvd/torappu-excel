from ..common import BaseStruct


class RuneStageGroupData(BaseStruct):
    groupId: str
    activeRuneStages: list["RuneStageGroupData.RuneStageInst"]
    startTs: int
    endTs: int

    class RuneStageInst(BaseStruct):
        stageId: str
        activePackedRuneIds: list[str]
