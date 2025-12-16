from msgspec import field

from .act_auto_chess_bond_active_type import ActAutoChessBondActiveType
from .act_auto_chess_mode_difficulty_type import ActAutoChessModeDifficultyType
from .act_auto_chess_mode_type import ActAutoChessModeType
from .activity_common_milestone_data import ActivityCommonMilestoneData
from .auto_chess_chess_type import AutoChessChessType
from .auto_chess_count_type import AutoChessCountType
from .auto_chess_effect_choice_type import AutoChessEffectChoiceType
from .auto_chess_effect_counter_type import AutoChessEffectCounterType
from .auto_chess_effect_type import AutoChessEffectType
from .auto_chess_item_type import AutoChessItemType
from .blackboard import Blackboard
from .evolve_phase import EvolvePhase
from .item_bundle import ItemBundle
from .rarity_rank import RarityRank
from ..common import BaseStruct


class ActAutoChessData(BaseStruct):
    modeDataDict: dict[str, "ActAutoChessData.ActAutoChessModeData"]
    baseRewardDataList: "list[ActAutoChessData.ActAutoChessBaseRewardData]"
    bandDataListDict: dict[str, "ActAutoChessData.ActAutoChessBandData"]
    charChessDataDict: dict[str, "ActAutoChessData.ActAutoChessCharChessData"]
    diyChessDict: dict[str, RarityRank]
    shopLevelDataDict: dict[str, dict[str, "ActAutoChessData.ActAutoChessShopLevelData"]]
    shopLevelDisplayDataDict: dict[str, "ActAutoChessData.ActAutoChessShopLevelDisplayData"]
    charShopChessDatas: dict[str, "ActAutoChessData.ActAutoChessCharShopChessData"]
    trapChessDataDict: dict[str, "ActAutoChessData.ActAutoChessTrapChessData"]
    trapShopChessDatas: dict[str, "ActAutoChessData.ActAutoChessTrapShopChessData"]
    stageDatasDict: dict[str, "ActAutoChessData.ActAutoChessStageData"]
    battleDataDict: dict[str, dict[str, "list[ActAutoChessData.ActAutoChessBattleData]"]]
    bondInfoDict: dict[str, "ActAutoChessData.ActAutoChessBondInfo"]
    garrisonDataDict: dict[str, "ActAutoChessData.ActAutoChessGarrisonData"]
    effectInfoDataDict: dict[str, "ActAutoChessData.ActAutoChessEffectInfoData"]
    effectBuffInfoDataDict: dict[str, "list[ActAutoChessData.ActAutoChessBuffInfoData]"]
    effectChoiceInfoDict: dict[str, "ActAutoChessData.ActAutoChessEffectChoiceInfoData"]
    bossInfoDict: dict[str, "ActAutoChessData.ActAutochessBossEntry"]
    specialEnemyInfoDict: dict[str, "ActAutoChessData.ActAutochessSpecialEnemyEntry"]
    enemyInfoDict: dict[str, list[str]]
    specialEnemyRandomTypeDict: dict[str, "ActAutoChessData.ActAutochessSpecialEnemyTypeEntry"]
    trainingNpcList: "list[ActAutoChessData.ActAutoChessTrainingNpcData]"
    milestoneList: list[ActivityCommonMilestoneData]
    modeFactorInfo: dict[str, float]
    difficultyFactorInfo: dict[str, float]
    playerTitleDataDict: dict[str, "ActAutoChessData.ActAutoChessPlayerTitleData"]
    shopCharChessInfoData: dict[str, "list[ActAutoChessData.ActAutoChessShopCharChessInfoData]"]
    constData: "ActAutoChessData.ActAutoChessConstData"
    chessNormalIdLookupDict: dict[str, str] | None = field(default=None)

    class ActAutoChessModeData(BaseStruct):
        modeId: str
        name: str
        code: str
        sortId: int
        backgroundId: str
        desc: str
        effectDescList: list[str]
        preposedMode: str | None
        unlockText: str | None
        loadingPicId: str
        modeType: ActAutoChessModeType
        modeDifficulty: ActAutoChessModeDifficultyType
        modeIconId: str
        modeColor: str
        specialPhaseTime: int
        activeBondIdList: list[str]
        inactiveBondIdList: list[str]
        inactiveEnemyKey: list[str]

    class ActAutoChessBondInfo(BaseStruct):
        bondId: str
        name: str
        desc: str
        iconId: str
        activeCount: int
        effectId: str
        activeType: ActAutoChessBondActiveType
        identifier: int
        weight: int
        isActiveInDeck: bool
        descParamBaseList: list[str]
        descParamPerStackList: list[str]
        noStack: bool
        chessIdList: list[str]

    class ActAutoChessGarrisonData(BaseStruct):
        garrisonDesc: str
        eventType: str
        eventTypeDesc: str
        eventTypeIcon: str
        eventTypeSmallIcon: str
        effectType: str
        charLevel: int
        battleRuneKey: str | None
        blackboard: "list[Blackboard]"
        description: str

    class ActAutoChessBandData(BaseStruct):
        bandId: str
        sortId: int
        modeTypeList: list[str]
        bandDesc: str
        totalHp: int
        effectId: str
        victorCount: int
        bandRewardModulus: float

    class ActAutoChessCharChessStatusData(BaseStruct):
        evolvePhase: EvolvePhase
        charLevel: int
        skillLevel: int
        favorPoint: int
        equipLevel: int

    class ActAutoChessCharChessData(BaseStruct):
        chessId: str
        identifier: int
        isGolden: bool
        status: "ActAutoChessData.ActAutoChessCharChessStatusData"
        upgradeChessId: str | None
        upgradeNum: int
        bondIds: list[str]
        garrisonIds: list[str] | None

    class ActAutoChessShopLevelData(BaseStruct):
        shopLevel: int
        initialUpgradePrice: int
        charChessCount: int
        itemCount: int
        levelTagBgColor: str

    class ActAutoChessShopCharChessInfoData(BaseStruct):
        chessLevel: int
        isGolden: bool
        evolvePhase: EvolvePhase
        charLevel: int
        skillLevel: int
        favorPoint: int
        equipLevel: int
        purchasePrice: int
        chessSoldPrice: int
        eliteIconId: str

    class ActAutoChessShopLevelDisplayData(BaseStruct):
        shopLevel: int
        levelTagBgColor: str
        isLevelCharChessEmpty: bool
        isLevelTrapChessEmpty: bool
        charChessDiySlotIdList: list[str] | None

    class ActAutoChessCharShopChessData(BaseStruct):
        chessId: str
        goldenChessId: str
        chessLevel: int
        shopLevelSortId: int
        chessType: AutoChessChessType
        charId: str | None
        tmplId: str | None
        defaultSkillIndex: int
        defaultUniEquipId: str | None
        backupCharId: str | None
        backupTmplId: str | None
        backupCharSkillIndex: int
        backupCharUniEquipId: str | None
        backupCharPotRank: int
        isHidden: bool

    class AutoChessTrapChessStatusData(BaseStruct):
        evolvePhase: EvolvePhase
        trapLevel: int
        skillIndex: int
        skillLevel: int

    class ActAutoChessTrapChessData(BaseStruct):
        chessId: str
        identifier: int
        charId: str
        isGolden: bool
        purchasePrice: int
        status: "ActAutoChessData.AutoChessTrapChessStatusData"
        upgradeChessId: str | None
        upgradeNum: int
        trapDuration: int
        effectId: str
        giveBondId: str | None
        givePowerId: str | None
        canGiveBond: bool
        itemType: AutoChessItemType

    class ActAutoChessTrapShopChessData(BaseStruct):
        itemId: str
        goldenItemId: str | None
        hideInShop: bool
        itemLevel: int
        iconLevel: int
        shopLevelSortId: int
        itemType: AutoChessItemType
        trapId: str

    class ActAutoChessStageData(BaseStruct):
        stageId: str
        mode: list[str]
        weight: int

    class ActAutoChessBattleData(BaseStruct):
        bossId: str | None
        levelId: str
        isSpPrepare: bool

    class ActAutoChessEffectInfoData(BaseStruct):
        effectId: str
        effectType: AutoChessEffectType
        effectCounterType: AutoChessEffectCounterType
        continuedRound: int
        effectName: str
        effectDesc: str
        effectDecoIconId: str | None
        enemyPrice: int

    class ActAutoChessBuffInfoData(BaseStruct):
        key: str
        blackboard: "list[Blackboard]"
        countType: AutoChessCountType

    class ActAutoChessEffectChoiceInfoData(BaseStruct):
        choiceEventId: str
        choiceType: AutoChessEffectChoiceType
        effectType: AutoChessEffectType
        name: str
        desc: str
        typeTxtColor: str

    class ActAutoChessPlayerTitleData(BaseStruct):
        id: str
        picId: str
        txt: str

    class ActAutochessBossEntry(BaseStruct):
        bossId: str
        sortId: int
        weight: int
        bloodPoint: int
        bloodPointNormal: int
        bloodPointHard: int
        isHidingBoss: bool

    class ActAutochessSpecialEnemyEntry(BaseStruct):
        type: str
        specialEnemyKey: str
        randomWeight: int
        isInFirstHalf: bool
        attachedNormalEnemyKeys: list[str]
        attachedEliteEnemyKeys: list[str]

    class ActAutochessSpecialEnemyTypeEntry(BaseStruct):
        count: int
        weight: int

    class ActAutoChessBaseRewardData(BaseStruct):
        round: int
        item: ItemBundle
        dailyMissionPoint: int

    class ActAutoChessTrainingNpcData(BaseStruct):
        npcId: str
        charId: str
        nameCardSkinId: str
        medalCount: int
        bandId: str

    class ActAutoChessConstData(BaseStruct):
        shopRefreshPrice: int
        maxDeckChessCnt: int
        maxBattleChessCnt: int
        fallbackBondId: str
        storeCntMax: int
        costPlayerHpLimit: int
        milestoneId: str
        borrowCount: int
        dailyMissionParam: int
        dailyMissionName: str
        dailyMissionRule: str
        trstageBandId: str
        trstageBossId: str
        trStageId: str
        trainingModeId: str
        trSpecialEnemyTypes: list[str]
        trBondIds: list[str]
        trBannedBondIds: list[str]
        milestoneTrackId: str
        bandNextUpdateTs: int
        escapedBattleTemplateMapSinglePlayer: str
        escapedBattleTemplateMapMultiPlayer: str
        webBusType: str
