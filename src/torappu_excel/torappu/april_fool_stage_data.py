from pydantic import BaseModel, ConfigDict

from .appearance_style import AppearanceStyle
from .item_bundle import ItemBundle
from .level_data import LevelData
from .stage_data import StageData


class AprilFoolStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    levelId: str
    code: str
    name: str
    appearanceStyle: AppearanceStyle
    loadingPicId: str
    difficulty: LevelData.Difficulty
    unlockCondition: list[StageData.ConditionDesc] | None
    stageDropInfo: list[ItemBundle]
