from msgspec import field

from .roguelike_bank_reward_count_type import RoguelikeBankRewardCountType
from .roguelike_event_type import RoguelikeEventType
from .roguelike_reward_ex_drop_tag_src_type import RoguelikeRewardExDropTagSrcType
from ..common import BaseStruct


class RoguelikeGameConst(BaseStruct):
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
    specialFailZoneId: str | None = field(default=None)
    unlockRouteItemCount: int | None = field(default=None)
    expeditionSelectDescFormat: str | None = field(default=None)
    travelLeaveToastFormat: str | None = field(default=None)
    charSelectTravelConflictToast: str | None = field(default=None)
    travelReturnDescUpgrade: str | None = field(default=None)
    travelReturnDesc: str | None = field(default=None)
    travelReturnDescItem: str | None = field(default=None)
    traderReturnTitle: str | None = field(default=None)
    traderReturnDesc: str | None = field(default=None)
    refreshNodeItemId: str | None = field(default=None)
