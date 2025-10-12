from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

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


class StageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
    sixStarStageId: str | None
    dangerLevel: str | None
    dangerPoint: int | float
    loadingPicId: str
    canPractice: bool
    canBattleReplay: bool
    apCost: int
    apFailReturn: int
    maxSlot: int
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
    canMultipleBattle: bool
    sixStarBaseDesc: str | None
    sixStarDisplayRewardList: list[ItemBundle] | None
    advancedRuneIdList1: list[str]
    advancedRuneIdList2: list[str]
    canUseCharm: bool | None = Field(default=None)
    canUseTech: bool | None = Field(default=None)
    canUseTrapTool: bool | None = Field(default=None)
    canUseBattlePerformance: bool | None = Field(default=None)
    canContinuousBattle: bool | None = Field(default=None)
    extraCondition: list["StageData.ExtraConditionDesc"] | None = Field(default=None)
    extraInfo: list["StageData.SpecialStoryInfo"] | None = Field(default=None)

    class StageDropInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        firstPassRewards: list[ItemBundle] | None
        firstCompleteRewards: list[ItemBundle] | None
        passRewards: list[list[WeightItemBundle]] | None
        completeRewards: list[list[WeightItemBundle]] | None
        displayRewards: list["StageData.DisplayRewards"]
        displayDetailRewards: list["StageData.DisplayDetailRewards"]

    class DisplayRewards(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        type: ItemType
        id: str
        dropType: StageDropType

    class DisplayDetailRewards(DisplayRewards):
        occPercent: OccPer

    class ConditionDesc(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        completeState: PlayerBattleRank

    class ExtraConditionDesc(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        index: int
        template: str
        unlockParam: list[str]

    class SpecialStoryInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        rewards: list[ItemBundle]
        progressInfo: "StageData.SpecialProgressInfo"
        imageId: str
        keyItemId: str | None
        unlockDesc: str | None

    class SpecialProgressInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        progressType: "StageData.SpecialStageUnlockProgressType"
        descList: dict[str, str] | None
