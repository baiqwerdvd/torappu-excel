from msgspec import field

from .item_bundle import ItemBundle
from .sub_profession_attack_type import SubProfessionAttackType
from .term_description_data import TermDescriptionData
from ..common import BaseStruct


class GameDataConsts(BaseStruct):
    addedRewardDisplayZone: str
    advancedGachaCrystalCost: int
    announceWebBusType: str
    charRotationPresetMaxCnt: int
    charRotationSkinListMaxCnt: int
    defaultCRPresetCharId: str
    defaultCRPresetCharSkinId: str
    defaultCRPresetBGId: str
    defaultCRPresetThemeId: str
    defaultCRPresetName: str
    charRotationPresetTrackTs: int
    uniequipArchiveSysTrackTs: int
    apBuyCost: int
    apBuyThreshold: int
    assistBeUsedSocialPt: dict[str, int]
    attackMax: float
    baseMaxFriendNum: int
    maxStarFriendNum: int
    maxSquadAssistDisplayNum: int
    friendStarEditTrackTs: int
    buyApTimeNoLimitFlag: bool
    characterExpMap: list[list[int]]
    characterUpgradeCostMap: list[list[int]]
    charAssistRefreshTime: list["GameDataConsts.CharAssistRefreshTimeState"]
    charmEquipCount: int
    commonPotentialLvlUpCount: int
    completeCrystalBonus: int
    completeGainBonus: float
    creditLimit: int
    dataVersion: str
    defCDPrimColor: str
    defCDSecColor: str
    defMax: float
    diamondMaterialToShardExchangeRatio: int
    diamondHandbookStageGain: int
    diamondToShdRate: int
    easyCrystalBonus: int
    evolveGoldCost: list[list[int]]
    friendAssistRarityLimit: list[int]
    hardDiamondDrop: int
    hpMax: float
    initCampaignTotalFee: int
    initCharIdList: list[str]
    initPlayerDiamondShard: int
    initPlayerGold: int
    initRecruitTagList: list[int]
    instFinDmdShdCost: int
    isClassicGachaPoolFuncEnabled: bool
    isClassicPotentialItemFuncEnabled: bool
    isClassicQCShopEnabled: bool
    isSpecialGachaPoolFuncEnabled: bool
    isDynIllustEnabled: bool
    isDynIllustStartEnabled: bool
    isLMGTSEnabled: bool
    isRoguelikeAvgAchieveFuncEnabled: bool
    isRoguelikeTopicFuncEnabled: bool
    legacyItemList: list[ItemBundle]
    legacyTime: int
    lMTGSDescConstOne: str
    lMTGSDescConstTwo: str
    LMTGSToEPGSRatio: int
    mailBannerType: list[str]
    mainlineCompatibleDesc: str
    mainlineEasyDesc: str
    mainlineNormalDesc: str
    mainlineToughDesc: str
    mainGuideActivedStageId: str
    maxLevel: list[list[int]]
    maxPlayerLevel: int
    maxPracticeTicket: int
    monthlySubRemainTimeLimitDays: int
    monthlySubWarningTime: int
    multiInComeByRank: list[str]
    newBeeGiftEPGS: int
    normalGachaUnlockPrice: list[int]
    normalRecruitLockedString: list[str]
    oneDiamondAp: int
    playerApMap: list[int]
    playerApRegenSpeed: int
    playerExpMap: list[int]
    pullForces: list[float]
    pullForceZeroIndex: int
    pushForces: list[float]
    pushForceZeroIndex: int
    recruitPoolVersion: int
    rejectSpCharMission: int
    reMax: float
    replicateShopStartTime: int
    requestSameFriendCD: int
    resPrefVersion: str
    richTextStyles: dict[str, str]
    storyReviewUnlockItemLackTip: str
    termDescriptionDict: dict[str, TermDescriptionData]
    UnlimitSkinOutOfTime: int
    useAssistSocialPt: int
    useAssistSocialPtMaxCount: int
    v006RecruitTimeStep1Refresh: int
    v006RecruitTimeStep2Check: int
    v006RecruitTimeStep2Flush: int
    voucherDiv: int
    voucherSkinDesc: str
    voucherSkinRedeem: int
    weeklyOverrideDesc: str
    TSO: int
    manufactPromptTime: int
    videoPlayerWebBusType: str
    gachaLogBusType: str
    defaultMinMultipleBattleTimes: int
    defaultMaxMultipleBattleTimes: int
    multipleActionOpen: bool
    birthdaySettingDesc: str
    birthdaySettingConfirmDesc: str
    birthdaySettingLeapConfirmDesc: str
    leapBirthdayRewardMonth: int
    leapBirthdayRewardDay: int
    birthdaySettingShowStageId: str
    isBirthdayFuncEnabled: bool
    isRecalRuneFuncEnabled: bool
    feverGameData: "GameDataConsts.FeverGameData"
    isSoCharEnabled: bool
    isVoucherClassicItemDistinguishable: bool = False
    operatorRecordsStartTime: int = -1
    subProfessionDamageTypePairs: dict[str, SubProfessionAttackType] = field(default_factory=dict)
    crisisUnlockStage: str = ""
    isSandboxPermFuncEnabled: bool = False
    classicProtectChar: list[str] = field(default_factory=list)
    continuousActionOpen: bool = False
    defaultMinContinuousBattleTimes: int = -1
    defaultMaxContinuousBattleTimes: int = -1

    class CharAssistRefreshTimeState(BaseStruct):
        Hour: int
        Minute: int

    class FeverGameData(BaseStruct):
        feverDuration: float
        feverNeed: float
