from .evolve_phase import EvolvePhase
from .roguelike_topic_mode import RoguelikeTopicMode
from ..common import BaseStruct

from msgspec import field


class RoguelikeTopicDetailConst(BaseStruct):
    playerLevelTable: dict[str, "RoguelikeTopicDetailConst.PlayerLevelData"]
    charUpgradeTable: dict[str, "RoguelikeTopicDetailConst.CharUpgradeData"]
    difficultyUpgradeRelicDescTable: dict[str, str]
    tokenBpId: str
    tokenOuterBuffId: str
    previewedRewardsAccordingUpdateId: str
    tipButtonName: str
    collectButtonName: str
    bpSystemName: str
    autoSetKV: str
    bpPurchaseActiveEnroll: str | None
    defaultSacrificeDesc: str | None
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
    gotCharBuffToast: str | None = field(default=None)
    predefinedLevelTable: dict[str, "RoguelikeTopicDetailConst.PredefinedPlayerLevelData"] | None = field(default=None)
    endingIconBorderDifficulty: int = field(default=0)
    endingIconBorderCount: int = field(default=0)

    class PlayerLevelData(BaseStruct):
        exp: int
        populationUp: int
        squadCapacityUp: int
        battleCharLimitUp: int
        maxHpUp: int

    class CharUpgradeData(BaseStruct):
        evolvePhase: EvolvePhase
        skillLevel: int
        skillSpecializeLevel: int

    class PredefinedPlayerLevelData(BaseStruct):
        levels: dict[str, "RoguelikeTopicDetailConst.PlayerLevelData"]
