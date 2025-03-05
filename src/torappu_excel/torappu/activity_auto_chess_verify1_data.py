from .act1_v_auto_chess_comment_report_count_type import (
    Act1VAutoChessCommentReportCountType,
)
from .act1_v_auto_chess_count_type import Act1VAutoChessCountType
from .act1_v_auto_chess_effect_counter_type import Act1VAutoChessEffectCounterType
from .act1_v_auto_chess_effect_type import Act1VAutoChessEffectType
from .act1_v_auto_chess_mode_type import Act1VAutoChessModeType
from .act1_v_auto_chess_shop_token_display_type import (
    Act1VAutoChessShopTokenDisplayType,
)
from .act1_v_auto_chess_trap_chess_type import Act1VAutoChessTrapChessType
from .auto_chess_skill_trigger_type import AutoChessSkillTriggerType
from .blackboard import Blackboard
from .evolve_phase import EvolvePhase
from .item_bundle import ItemBundle
from .profession_category import ProfessionCategory
from .rarity_rank import RarityRank
from ..common import BaseStruct

from msgspec import field


class ActivityAutoChessVerify1Data(BaseStruct):
    modeDataList: list["ActivityAutoChessVerify1Data.Act1VAutoChessModeData"]
    baseRewardDataDict: dict[str, list["ActivityAutoChessVerify1Data.Act1VAutoChessBaseRewardData"]]
    mileStoneList: list["ActivityAutoChessVerify1Data.Act1VAutoChessMilestoneData"]
    bandDataListDict: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessBandData"]
    forceDataListDict: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessForceData"]
    shopLevelDataDict: dict[str, list["ActivityAutoChessVerify1Data.Act1VAutoChessShopLevelData"]]
    shopLevelDisplayDataDict: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessShopLevelDisplayData"]
    skillTriggerDataList: list["ActivityAutoChessVerify1Data.Act1VAutoChessSkillTriggerData"]
    battleCommentDataList: list["ActivityAutoChessVerify1Data.Act1VAutoChessBattleCommentData"]
    shopStateTokenData: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessShopStateTokenData"]
    effectInfoDataDict: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessEffectInfoData"]
    cultivateEffectList: list["ActivityAutoChessVerify1Data.Act1VAutoChessCultivateRelationData"]
    diyChessSlotDataDict: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessDiyChessSlotData"]
    effectBuffInfoDataDict: dict[str, list["ActivityAutoChessVerify1Data.Act1VAutoChessBuffInfoData"]]
    constData: "ActivityAutoChessVerify1Data.Act1VAutoChessConstData"
    charShopChessDatas: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessCharShopChessData"]
    charChessDataDict: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessCharChessData"]
    chessNormalIdLookupDict: dict[str, str]
    trapShopChessDatas: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessTrapShopChessData"]
    trapChessDataDict: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessTrapChessData"]
    stageDatasDict: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessStageData"]
    forceLevelDetailedDataDict: dict[str, list["ActivityAutoChessVerify1Data.Act1VAutoChessForceLevelRoundData"]]
    effectTypeDescriptionDict: dict[str, str | None]
    charFactionDict: dict[str, str]
    factionDatas: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessFactionData"]
    effectCounterTypeDataDict: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessEffectCounterTypeData"]

    class Act1VAutoChessModeData(BaseStruct):
        modeId: str
        sortId: int
        name: str
        desc: str
        preposedMode: str | None
        unlockText: str | None
        effectDescList: list[str]
        loadingPicId: str
        code: str
        modeType: Act1VAutoChessModeType

    class Act1VAutoChessBandData(BaseStruct):
        bandId: str
        sortId: int
        bandName: str
        bandIconId: str
        bandDesc: str
        totalHp: int
        initialEffectId: str
        charId: str
        charName: str
        unlockDesc: str | None

    class Act1VAutoChessModeBossHpData(BaseStruct):
        modeId: str
        hp: int

    class Act1VAutoChessForceData(BaseStruct):
        forceId: str
        sortId: int
        forceName: str
        forceIconId: str
        forceDesc: str
        leaderEnemyId: str
        leaderName: str
        modeHpDatas: list["ActivityAutoChessVerify1Data.Act1VAutoChessModeBossHpData"]

    class Act1VAutoChessBaseRewardData(BaseStruct):
        damageMin: int
        damageMax: int
        item: ItemBundle
        dailyMissionPoint: int

    class Act1VAutoChessMilestoneData(BaseStruct):
        milestoneId: str
        orderId: int
        tokenNum: int
        item: ItemBundle

    class Act1VAutoChessEffectInfoData(BaseStruct):
        effectId: str
        effectType: Act1VAutoChessEffectType
        effectCounterType: Act1VAutoChessEffectCounterType
        continuedRound: int
        effectName: str
        effectDesc: str
        effectDecoIconId: str | None
        isMainEnemyEffect: bool

    class Act1VAutoChessCultivateRelationData(BaseStruct):
        cultivateNum: int
        effectId: str
        evolvePhase: EvolvePhase
        charLevel: int
        atkPer: int
        defPer: int
        hpPer: int

    class Act1VAutoChessShopLevelData(BaseStruct):
        shopLevel: int
        initialUpgradePrice: int
        chessCount: int
        itemCount: int
        baseShieldValue: int

    class Act1VAutoChessShopLevelDisplayData(BaseStruct):
        shopLevel: int
        levelTagBgColor: str
        isLevelCharChessEmpty: bool
        isLevelTrapChessEmpty: bool
        charChessDiySlotIdList: list[str] | None

    class Act1VAutoChessCharShopChessData(BaseStruct):
        chessId: str
        goldenChessId: str
        isDiyChessSlot: bool
        chessLevel: int
        shopLevelSortId: int
        canBeRented: bool
        charId: str | None
        tmplId: str | None
        defaultSkillIndex: int
        defaultUniEquipId: str | None
        backupCharId: str | None
        backupCharRepName: str | None
        backupCharSkillIndex: int
        backupCharUniEquipId: str | None
        backupCharPotRank: int

    class Act1VAutoChessCharChessStatusData(BaseStruct):
        evolvePhase: EvolvePhase
        charLevel: int
        skillLevel: int
        favorPoint: int
        equipLevel: int
        maxItemEquipCnt: int

    class Act1VAutoChessCharChessData(BaseStruct):
        chessId: str
        isGolden: bool
        purchasePrice: int
        status: "ActivityAutoChessVerify1Data.Act1VAutoChessCharChessStatusData"
        upgradeChessId: str | None
        upgradeNum: int
        damage: int

    class Act1VAutoChessTrapChessStatusData(BaseStruct):
        evolvePhase: EvolvePhase
        trapLevel: int
        skillIndex: int
        skillLevel: int

    class Act1VAutoChessTrapChessData(BaseStruct):
        chessId: str
        isGolden: bool
        purchasePrice: int
        status: "ActivityAutoChessVerify1Data.Act1VAutoChessTrapChessStatusData"
        upgradeChessId: str | None
        upgradeNum: int
        trapDuration: int
        effectId: str
        giveGroupId: str | None
        itemType: Act1VAutoChessTrapChessType

    class Act1VAutoChessForceLevelRoundData(BaseStruct):
        round: int
        roundData: dict[str, "ActivityAutoChessVerify1Data.Act1VAutoChessForceLevelDetailedData"]

    class Act1VAutoChessForceLevelDetailedData(BaseStruct):
        forceId: str
        levelId: str
        roundDetailId: str
        round: int

    class Act1VAutoChessStageData(BaseStruct):
        stageId: str
        mode: list[str]
        weight: int

    class Act1VAutoChessTrapShopChessData(BaseStruct):
        itemId: str
        goldenItemId: str | None
        hideInChessShop: bool
        itemLevel: int
        iconLevel: int
        shopLevelSortId: int
        itemType: Act1VAutoChessTrapChessType
        trapId: str

    class Act1VAutoChessDiyChessSlotData(BaseStruct):
        charRarity: RarityRank

    class Act1VAutoChessTurnInfoData(BaseStruct):
        round: int
        rewardEnemyPreview: bool

    class Act1VAutoChessBuffInfoData(BaseStruct):
        key: str
        blackboard: list[Blackboard]
        countType: Act1VAutoChessCountType

    class Act1VAutoChessFactionData(BaseStruct):
        factionId: str
        factionName: str
        sortId: int

    class Act1VAutoChessBattleCommentData(BaseStruct):
        template: str
        description: str
        reportType: Act1VAutoChessCommentReportCountType
        blackboard: list[Blackboard]

    class Act1VAutoChessConstData(BaseStruct):
        chessSoldPrice: int
        shopRefreshPrice: int
        bonusRound: int
        maxDeckCnt: int
        maxChessCnt: int
        deltaShopUpgradePrice: int
        shieldToDmgScale: int
        spellCntLimit: int
        costPlayerHpLimit: int
        rewardEnemyGroupKey: str
        rewardEnemyEffectId: str
        selfDefenseDamageTip: str
        selfCharDamageTip: str
        selfDamageTip: str
        selfSpecialDamageTip: str
        additionalAwardCount1: int
        additionalAwardCount2: int
        normalAwardTxt: str
        additionalAwardTxt: str
        milestoneId: str
        boxChangeTxt: str
        startCd: int
        borrowCount: int
        maxBorrowListCnt: int
        dailyMissionParam: int
        dailyMissionRewardId: str
        dailyMissionRewardType: str
        dailyMissionRewardCount: int
        dailyMissionName: str
        dailyMissionDesc: str
        dailyMissionRule: str
        defaultFaction: "ActivityAutoChessVerify1Data.Act1VAutoChessFactionData"
        utilTrapIds: list[str]
        specialRescuitIds: list[str]
        rewardSkinId: str
        rewardSkinText: str
        rewardAvatarId: str
        rewardAvatarText: str
        forceFocusEnemyTurns: list[int]
        tutorialPhase1Round: int
        tutorialPhase2Round: int
        tutorialPhase3Round: int
        tutorialPhase1ShopLevel: int
        tutorialPhase2ShopLevel: int

    class Act1VAutoChessSkillTriggerData(BaseStruct):
        profession: ProfessionCategory
        subProfessionId: str | None
        charId: str | None
        skillIndex: int
        skillTriggerType: AutoChessSkillTriggerType

    class Act1VAutoChessShopStateTokenData(BaseStruct):
        tokenId: str
        tokenDisplayType: Act1VAutoChessShopTokenDisplayType

    class Act1VAutoChessEffectCounterTypeData(BaseStruct):
        type_: Act1VAutoChessEffectCounterType = field(name="type")
        format_: str = field(name="format")
