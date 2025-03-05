from .item_bundle import ItemBundle
from .sandbox_v2_diff_mode_data import SandboxV2DiffModeData
from ..common import BaseStruct

from msgspec import field


class SandboxV2BasicConst(BaseStruct):
    staminaItemId: str
    goldItemId: str
    dimensioncoinItemId: str
    alwaysShowItemIdsConstruct: list[str]
    alwaysShowItemIds: list[str]
    bagBottomBarResType: list[str]
    failedCookFood: str
    maxFoodDuration: int
    drinkCostOnce: int
    drinkMakeLimit: int
    specialMatWater: str
    workbenchMakeLimit: int
    logisticsPosLimit: int
    logisticsUnlockLevel: int
    logisticsDrinkCost: int
    logisticsEvacuateTips: str
    logisticsEvacuateWarning: str
    baseRepairCost: int
    portRepairCost: int
    unitFenceLimit: int
    unitRareFenceLimit: int
    cageId: str
    fenceId: str
    rareFenceId: str | None
    monthlyRushEntryText1: str | None
    monthlyEntryUnlockText: str
    monthlyEntryRiftText: str
    monthlyRushIntro: str
    monthlyCoin: ItemBundle
    charRarityColorList: list[str]
    squadCharCapacity: int
    totalSquadCnt: int
    toolboxCapacity: int
    toolCntLimitInSquad: int
    miniSquadCharCapacity: int
    miniSquadDrinkCost: int
    normalSquadDrinkCost: int
    emptySquadDrinkCost: int
    achieveTypeAll: str
    constructModeBgmHome: str
    battleBgmCollect: str
    battleBgmHunt: str
    battleBgmEnemyRush: str
    battleBgmBossRush: str
    imgLoadingNormalName: str
    imgLoadingBaseName: str
    imgUnloadingBaseName: str
    isChallengeOpen: bool
    isRacingOpen: bool
    hasExploreMode: bool
    exploreModeBuffDescs: list[str] | None
    modeSelectTips: str
    stringRes: dict[str, str] | None
    diffList: list[SandboxV2DiffModeData]
    battlePreloadEnemies: list[str]
    battleExcludedTrapsInRush: list[str]
    enhancedSubFoodmat: str | None = field(default=None)
    enhancedDuration: int | None = field(default=None)
