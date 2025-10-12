from pydantic import BaseModel, ConfigDict, Field

from .roguelike_bank_reward_count_type import RoguelikeBankRewardCountType
from .roguelike_event_type import RoguelikeEventType
from .roguelike_reward_ex_drop_tag_src_type import RoguelikeRewardExDropTagSrcType


class RoguelikeGameConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    initSceneName: str
    failSceneName: str
    hpItemId: str
    goldItemId: str
    populationItemId: str
    squadCapacityItemId: str
    expItemId: str
    initialBandShowGradeFlag: bool
    bankMaxGold: int
    bankCostId: str | None
    bankDrawCount: int
    bankDrawLimit: int
    bankRewardCountType: RoguelikeBankRewardCountType
    spZoneShopBgmSignal: str | None
    mimicEnemyIds: list[str]
    bossIds: list[str]
    goldChestTrapId: str
    normBoxTrapId: str | None
    rareBoxTrapId: str | None
    badBoxTrapId: str | None
    maxHpItemId: str | None
    shieldItemId: str | None
    keyItemId: str | None
    divinationKitItemId: str | None
    chestKeyCnt: int
    chestKeyItemId: str | None
    keyColorId: str | None
    onceNodeTypeList: list[RoguelikeEventType]
    vertNodeCostDialogUseItemIconType: bool
    gpScoreRatio: int
    overflowUsageSquadBuff: str | None
    specialTrapId: str | None
    trapRewardRelicId: str | None
    unlockRouteItemId: str | None
    hideBattleNodeName: str | None
    hideBattleNodeDescription: str | None
    hideNonBattleNodeName: str | None
    hideNonBattleNodeDescription: str | None
    charSelectExpeditionConflictToast: str | None
    charSelectNoUpgradeConflictToast: str | None
    itemDropTagDict: dict[RoguelikeRewardExDropTagSrcType, str]
    shopRefreshCostId: str | None
    expeditionLeaveToastFormat: str | None
    expeditionReturnDescCureUpgrade: str | None
    expeditionReturnDescUpgrade: str | None
    expeditionReturnDescCure: str | None
    expeditionReturnDesc: str | None
    expeditionReturnDescItem: str | None
    expeditionReturnRewardBlackList: list[str]
    candleReturnDescCandleUpgrade: str | None
    candleReturnDescCandle: str | None
    charSelectCandleConflictToast: str | None
    charSelectGuidedConflictToast: str | None
    charSelectNonGuidedConflictToast: str | None
    gainBuffDiffGrade: int
    dsPredictTips: str | None
    dsBuffActiveTips: str | None
    totemDesc: str | None
    copperGildDesc: str | None
    relicDesc: str | None
    buffDesc: str | None
    storingRecruitDesc: str | None
    storingRecruitSucceedToast: str | None
    specialRecruitReductionDesc: str | None
    specialRecruitFuncDesc: str | None
    specialRecruitDetailDesc: str | None
    portalZones: list[str]
    diffDisplayZoneId: str | None
    exploreExpOnKill: str | None
    fusionName: str | None
    fusionNotifyToast: str | None
    haveSpZone: bool
    gotCharCandleBuffToast: str | None
    gotCharsCandleBuffToast: str | None
    stashedRecruitNodeDescription: str | None
    stashedRecruitEmptyNodeDescription: str | None
    recruitStashMaxNum: int
    recruitStashMinNum: int
    hasTopicCharSelectMenuButton: bool
    specialFailZoneId: str | None = Field(default=None)
    unlockRouteItemCount: int | None = Field(default=None)
    expeditionSelectDescFormat: str | None = Field(default=None)
    travelLeaveToastFormat: str | None = Field(default=None)
    charSelectTravelConflictToast: str | None = Field(default=None)
    travelReturnDescUpgrade: str | None = Field(default=None)
    travelReturnDesc: str | None = Field(default=None)
    travelReturnDescItem: str | None = Field(default=None)
    traderReturnTitle: str | None = Field(default=None)
    traderReturnDesc: str | None = Field(default=None)
    refreshNodeItemId: str | None = Field(default=None)
