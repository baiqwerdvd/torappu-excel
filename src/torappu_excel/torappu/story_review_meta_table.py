from pydantic import BaseModel, ConfigDict

from .act_archive_component_table import ActArchiveComponentTable
from .act_archive_res_data import ActArchiveResData
from .mini_act_trial_data import MiniActTrialData
from .training_camp_data import TrainingCampData


class StoryReviewMetaTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    miniActTrialData: MiniActTrialData
    actArchiveResData: ActArchiveResData
    actArchiveData: ActArchiveComponentTable
    trainingCampData: TrainingCampData
