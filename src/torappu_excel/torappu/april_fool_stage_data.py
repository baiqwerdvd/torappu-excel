from .appearance_style import AppearanceStyle
from .item_bundle import ItemBundle
from .level_data import LevelData
from .stage_data import StageData
from ..common import BaseStruct


class AprilFoolStageData(BaseStruct):
    stageId: str
    levelId: str
    code: str
    name: str
    appearanceStyle: AppearanceStyle
    loadingPicId: str
    difficulty: LevelData.Difficulty
    unlockCondition: list[StageData.ConditionDesc] | None
    stageDropInfo: list[ItemBundle]
