from .new_training_camp_stage_data import NewTrainingCampStageData
from .training_camp_consts import TrainingCampConsts
from .training_camp_stage_data import TrainingCampStageData
from ..common import BaseStruct


class TrainingCampData(BaseStruct):
    stageData: dict[str, TrainingCampStageData]
    newTrainingCampStages: list[NewTrainingCampStageData]
    consts: TrainingCampConsts
