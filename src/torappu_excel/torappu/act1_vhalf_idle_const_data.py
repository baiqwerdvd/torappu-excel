from .act1_vhalf_idle_enemy_preload_meta import Act1VHalfIdleEnemyPreloadMeta
from .profession_category import ProfessionCategory
from .rune_table import RuneTable
from ..common import BaseStruct


class Act1VHalfIdleConstData(BaseStruct):
    incomeProductionItems: list[str]
    milestoneId: str
    discount: list[int]
    skillLevels: list[int]
    levelExpItemId: str
    skillExpItemId: str
    normalStageIds: list[str]
    hardStageIds: list[str]
    techCostItemId: str
    assistBaseNum: int
    preloadEnemy: list[Act1VHalfIdleEnemyPreloadMeta]
    preloadTrap: list[str]
    defaultMaxDiscountSkillLevel: int
    npcMaxDiscountSkillLevel: int
    forbiddenAssistCharIds: list[str]
    maxEvolvePhase: int
    maxSafeEnemyDuration: int
    overloadLoseLifePoint: int
    trapModifyBossTriggerTime: int
    normalEnemyOverloadCnt: int
    eliteEnemyOverloadCnt: int
    bossEnemyOverloadCnt: int
    maxEquipNumInBag: int
    bossBranchName: str
    bossPreviewBranchName: str
    enemyCapacityIdWhiteList: list[str]
    unlockStageId: str
    professionDesc: list["Act1VHalfIdleConstData.ProfessionDesc"]
    productMaxEfficiencyDict: dict[str, int]
    efficiencyDurationMax: int
    produceCd: int
    harvestHintThresholdTime: int
    constRuneDatas: list["RuneTable.PackedRuneData"]
    milestoneTrackId: str
    maxDeckCardNum: int
    tutorialStageId: str
    predefinedPlotIds: list[str]
    predefinedCharIds: list[str]
    enemyOverloadWarningRatio: float
    battleFinishWarningTime: int
    gachaNumMax: int
    battleCustomTileHighlightColor: str
    battleCustomTileEmissionColor: str
    battleEquipLevelColors: list[str]
    battleFailHintStr: list[str]
    trapDropWeightStep: int
    unlockSpecialPlot: list[str]
    bossEnterBgmKey: str

    class ProfessionDesc(BaseStruct):
        profession: ProfessionCategory
        desc: str
