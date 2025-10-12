from pydantic import BaseModel, ConfigDict

from .new_training_camp_stage_data import NewTrainingCampStageData
from .training_camp_consts import TrainingCampConsts
from .training_camp_stage_data import TrainingCampStageData


class TrainingCampData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageData: dict[str, TrainingCampStageData]
    newTrainingCampStages: list[NewTrainingCampStageData]
    consts: TrainingCampConsts
