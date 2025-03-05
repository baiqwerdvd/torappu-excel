from enum import StrEnum

from .appearance_style import AppearanceStyle
from .item_bundle import ItemBundle
from .item_type import ItemType
from .level_data import LevelData
from .occ_per import OccPer
from .player_battle_rank import PlayerBattleRank
from .stage_diff_group import StageDiffGroup
from .stage_drop_type import StageDropType
from .stage_type import StageType
from .weight_item_bundle import WeightItemBundle
from ..common import BaseStruct

from msgspec import field


class StageData(BaseStruct):
    class PerformanceStageFlag(StrEnum):
        NORMAL_STAGE = "NORMAL_STAGE"
        PERFORMANCE_STAGE = "PERFORMANCE_STAGE"

    class SpecialStageUnlockProgressType(StrEnum):
        ONCE = "ONCE"
        PROGRESS = "PROGRESS"

    stageType: StageType
    difficulty: LevelData.Difficulty
    performanceStageFlag: "StageData.PerformanceStageFlag"
    diffGroup: StageDiffGroup
    unlockCondition: list["StageData.ConditionDesc"]
    stageId: str
    levelId: str | None
    zoneId: str
    code: str
    name: str | None
    description: str | None
    hardStagedId: str | None
    dangerLevel: str | None
    dangerPoint: int | float
    loadingPicId: str
    canPractice: bool
    canBattleReplay: bool
    apCost: int
    apFailReturn: int
    etItemId: str | None
    etCost: int
    etFailReturn: int
    etButtonStyle: str | None
    apProtectTimes: int
    diamondOnceDrop: int
    practiceTicketCost: int
    dailyStageDifficulty: int
    expGain: int
    goldGain: int
    loseExpGain: int
    loseGoldGain: int
    passFavor: int
    completeFavor: int
    slProgress: int
    displayMainItem: str | None
    hilightMark: bool
    bossMark: bool
    isPredefined: bool
    isHardPredefined: bool
    isSkillSelectablePredefined: bool
    isStoryOnly: bool
    appearanceStyle: AppearanceStyle
    stageDropInfo: "StageData.StageDropInfo"
    startButtonOverrideId: str | None
    isStagePatch: bool
    mainStageId: str | None
    canUseFirework: bool
    canUseCharm: bool | None = field(default=None)
    canUseTech: bool | None = field(default=None)
    canUseTrapTool: bool | None = field(default=None)
    canUseBattlePerformance: bool | None = field(default=None)
    canContinuousBattle: bool | None = field(default=None)
    extraCondition: list["StageData.ExtraConditionDesc"] | None = field(default=None)
    extraInfo: list["StageData.SpecialStoryInfo"] | None = field(default=None)

    class StageDropInfo(BaseStruct):
        firstPassRewards: list[ItemBundle] | None
        firstCompleteRewards: list[ItemBundle] | None
        passRewards: list[list[WeightItemBundle]] | None
        completeRewards: list[list[WeightItemBundle]] | None
        displayRewards: list["StageData.DisplayRewards"]
        displayDetailRewards: list["StageData.DisplayDetailRewards"]

    class DisplayRewards(BaseStruct):
        type_: ItemType = field(name="type")
        id_: str = field(name="id")
        dropType: StageDropType

    class DisplayDetailRewards(DisplayRewards):
        occPercent: OccPer

    class ConditionDesc(BaseStruct):
        stageId: str
        completeState: PlayerBattleRank

    class ExtraConditionDesc(BaseStruct):
        index: int
        template: str
        unlockParam: list[str]

    class SpecialStoryInfo(BaseStruct):
        stageId: str
        rewards: list[ItemBundle]
        progressInfo: "StageData.SpecialProgressInfo"
        imageId: str

    class SpecialProgressInfo(BaseStruct):
        progressType: "StageData.SpecialStageUnlockProgressType"
        descList: dict[str, str] | None
