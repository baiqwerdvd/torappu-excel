from ..common import BaseStruct


class TrainingCampStageData(BaseStruct):
    stageId: str
    stageIconId: str
    sortId: int
    levelId: str
    code: str
    name: str
    loadingPicId: str
    description: str
    endCharId: str
    updateTs: int
