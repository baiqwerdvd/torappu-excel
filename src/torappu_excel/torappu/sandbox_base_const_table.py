from ..common import BaseStruct


class SandboxBaseConstTable(BaseStruct):
    cookRegularCostItemId: str
    cookRegularCostItemIdCnt: int
    squadTabNameList: list[str]
    charRarityColorList: list[str]
    sumFoodLimitedCount: int
    sumBuildingLimitedCount: int
    sumTacticalLimitedCount: int
    sumFoodMatLimitedCount: int
    sumBuildingMatLimitedCount: int
    sumStaminaPotLimitedCount: int
    sumGoldLimitedCount: int
    itemLimitedCount: int
    blackBoxSlotCnt: int
    scoutNodeUpgradeId: str
    battleNodeUpgradeId: str
    staminaPotCostOnce: int
    staminaPotItemId: str
    staminapotRedMinCnt: int
    staminapotYellowMinCnt: int
    staminapotGreenMinCnt: int
    staminapotMaxPercentCnt: int
    staminaPotActionPoint: int
    goldItemId: str
    toolboxSlotCapacity: int
    toolboxSlotCnt: int
    teamPopulationLimit: int
    researchInformationDesc: str
    settleFailDesc: str
    settleAbortDesc: str
    settleSucDesc: str
