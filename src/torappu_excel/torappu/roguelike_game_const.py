from .roguelike_event_type import RoguelikeEventType
from .roguelike_reward_ex_drop_tag_src_type import RoguelikeRewardExDropTagSrcType
from ..common import BaseStruct

from msgspec import field


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
    mimicEnemyIds: list[str]
    bossIds: list[str]
    goldChestTrapId: str
    normBoxTrapId: str | None
    rareBoxTrapId: str | None
    badBoxTrapId: str | None
    maxHpItemId: str | None
    shieldItemId: str | None
    keyItemId: str | None
    chestKeyCnt: int
    chestKeyItemId: str | None
    keyColorId: str | None
    onceNodeTypeList: list[RoguelikeEventType]
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
    itemDropTagDict: dict[RoguelikeRewardExDropTagSrcType, str]
    expeditionLeaveToastFormat: str | None
    expeditionReturnDescCureUpgrade: str | None
    expeditionReturnDescUpgrade: str | None
    expeditionReturnDescCure: str | None
    expeditionReturnDesc: str | None
    expeditionReturnDescItem: str | None
    expeditionReturnRewardBlackList: list[str]
    gainBuffDiffGrade: int
    dsPredictTips: str | None
    dsBuffActiveTips: str | None
    totemDesc: str | None
    relicDesc: str | None
    buffDesc: str | None
    portalZones: list[str]
    exploreExpOnKill: str | None
    specialFailZoneId: str | None
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
