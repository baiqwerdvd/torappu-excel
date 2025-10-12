from pydantic import BaseModel, ConfigDict, Field

from .evolve_phase import EvolvePhase
from .roguelike_topic_mode import RoguelikeTopicMode


class RoguelikeTopicDetailConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    playerLevelTable: dict[str, "RoguelikeTopicDetailConst.PlayerLevelData"]
    charUpgradeTable: dict[str, "RoguelikeTopicDetailConst.CharUpgradeData"]
    difficultyUpgradeRelicDescTable: dict[str, str]
    tokenBpId: str
    tokenOuterBuffId: str
    spOperatorLockedMessage: str | None
    previewedRewardsAccordingUpdateId: str
    tipButtonName: str
    collectButtonName: str
    bpSystemName: str
    autoSetKV: str
    bpPurchaseActiveEnroll: str | None
    defaultExpeditionSelectDesc: str | None
    gotCharMutationBuffToast: str | None
    gotCharEvolutionBuffToast: str | None
    gotSquadBuffToast: str | None
    loseCharBuffToast: str | None
    monthTeamSystemName: str
    battlePassUpdateName: str
    monthCharCardTagName: str
    monthTeamDescTagName: str
    outerBuffCompleteText: str
    outerProgressTextColor: str
    copySeedModeInfo: str | None
    copySucceededTextHint: str | None
    historicalRecordsMode: RoguelikeTopicMode
    historicalRecordsCount: int
    historicalRecordsStartTime: int
    challengeTaskTargetName: str
    challengeTaskConditionName: str
    challengeTaskRewardName: str
    challengeTaskModeName: str
    challengeTaskName: str
    outerBuffTokenSum: int
    needAllFrontNode: bool
    showBlurBack: bool
    defaultSacrificeDesc: str | None = Field(default=None)
    gotCharBuffToast: str | None = Field(default=None)
    predefinedLevelTable: dict[str, "RoguelikeTopicDetailConst.PredefinedPlayerLevelData"] | None = Field(default=None)
    endingIconBorderDifficulty: int = Field(default=0)
    endingIconBorderCount: int = Field(default=0)

    class PlayerLevelData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        exp: int
        populationUp: int
        squadCapacityUp: int
        battleCharLimitUp: int
        maxHpUp: int

    class CharUpgradeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        evolvePhase: EvolvePhase
        skillLevel: int
        skillSpecializeLevel: int

    class PredefinedPlayerLevelData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        levels: dict[str, "RoguelikeTopicDetailConst.PlayerLevelData"]
