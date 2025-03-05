from ..common import BaseStruct


class NewTrainingCampStageData(BaseStruct):
    updateTs: int
    stages: list[str]
