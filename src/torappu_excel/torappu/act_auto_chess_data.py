from .act_auto_chess_bond_active_condition_type import ActAutoChessBondActiveConditionType
from .act_auto_chess_bond_active_type import ActAutoChessBondActiveType
from .act_auto_chess_bond_phase_type import ActAutoChessBondPhaseType
from .act_auto_chess_mode_difficulty_type import ActAutoChessModeDifficultyType
from .act_auto_chess_mode_group_type import ActAutoChessModeGroupType
from .act_auto_chess_mode_type import ActAutoChessModeType
from .act_auto_chess_multi_mode_sub_type import ActAutoChessMultiModeSubType
from .activity_common_milestone_data import ActivityCommonMilestoneData
from .activity_periodical_reward_conf import ActivityPeriodicalRewardConf
from .auto_chess_band_type import AutoChessBandType
from .auto_chess_chess_type import AutoChessChessType
from .auto_chess_data import AutoChessData
from .auto_chess_effect_choice_type import AutoChessEffectChoiceType
from .auto_chess_effect_counter_type import AutoChessEffectCounterType
from .auto_chess_effect_type import AutoChessEffectType
from .auto_chess_item_type import AutoChessItemType
from .auto_chess_selection_type import AutoChessSelectionType
from .auto_chess_skill_avail_type import AutoChessSkillAvailType
from .auto_chess_skill_type import AutoChessSkillType
from .blackboard import Blackboard
from .evolve_phase import EvolvePhase
from .rarity_rank import RarityRank
from .template_shop_data import TemplateShopData
from .vector2 import Vector2
from ..common import BaseStruct


class ActAutoChessData(BaseStruct):
    modeDataDict: dict[str, "ActAutoChessData.ActAutoChessModeData"]
    modeGroupDataDict: dict[str, "ActAutoChessData.ActAutoChessModeGroupData"]
    chessNormalIdLookupDict: dict[str, str]
    diyChessDict: dict[str, RarityRank]
    diyChessInfoDict: dict[str, list[str]]
    shopLevelDisplayDataDict: dict[str, "ActAutoChessData.ActAutoChessShopLevelDisplayData"]
    stageDatasDict: dict[str, "ActAutoChessData.ActAutoChessStageData"]
    enemyInfoDict: dict[str, list[str]]
    specialEnemyRandomTypeDict: dict[str, "ActAutoChessData.ActAutochessSpecialEnemyTypeEntry"]
    enemyRewardTypeDict: dict[str, str]
    enemyRewardTextFormatDict: dict[str, str]
    milestoneList: list[ActivityCommonMilestoneData]
    periodicalRewards: dict[str, ActivityPeriodicalRewardConf]
    modeFactorInfo: dict[str, float]
    difficultyFactorInfo: dict[str, float]
    playerTitleDataDict: dict[str, "ActAutoChessData.ActAutoChessPlayerTitleData"]
    shopCharChessInfoData: dict[str, "list[ActAutoChessData.ActAutoChessShopCharChessInfoData]"]
    constData: "ActAutoChessData.ActAutoChessConstData"
    seasonShop: TemplateShopData
    bandDataListDict: dict[str, "ActAutoChessData.ActAutoChessBandData"]
    bondInfoDict: dict[str, "ActAutoChessData.ActAutoChessBondInfo"]
    garrisonDataDict: dict[str, "ActAutoChessData.ActAutoChessGarrisonData"]
    effectDescParamDataDict: dict[str, "ActAutoChessData.ActAutoChessEffectDescParamData"]
    effectInfoDataDict: dict[str, "ActAutoChessData.ActAutoChessEffectInfoData"]
    skillInfoDataDict: dict[str, "ActAutoChessData.ActAutoChessSkillInfoData"]
    effectBuffInfoDataDict: dict[str, "list[ActAutoChessData.ActAutoChessBuffInfoData]"]
    shopLevelDataDict: dict[str, dict[str, "ActAutoChessData.ActAutoChessShopLevelData"]]
    charChessDataDict: dict[str, "ActAutoChessData.ActAutoChessCharChessData"]
    charShopChessDatas: dict[str, "ActAutoChessData.ActAutoChessCharShopChessData"]
    trapChessDataDict: dict[str, "ActAutoChessData.ActAutoChessTrapChessData"]
    trapShopChessDatas: dict[str, "ActAutoChessData.ActAutoChessTrapShopChessData"]
    effectChoiceInfoDict: dict[str, "ActAutoChessData.ActAutoChessEffectChoiceInfoData"]
    battleDataDict: dict[str, dict[str, "list[ActAutoChessData.ActAutoChessBattleData]"]]
    bossInfoDict: dict[str, "ActAutoChessData.ActAutochessBossEntry"]
    specialEnemyInfoDict: dict[str, "ActAutoChessData.ActAutochessSpecialEnemyEntry"]
    trainingNpcList: "list[ActAutoChessData.ActAutoChessTrainingNpcData]"
    trainingData: "ActAutoChessTrainingData"

    class ActAutoChessModeData(BaseStruct):
        modeId: str
        name: str
        code: str
        sortId: int
        backgroundId: str
        desc: str | None
        difficulty: int
        factor: float
        difficultyDesc: str
        trophyDesc: str | None
        eventIds: list[str]
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
        startTime: int
        unlockDiffierentModeId: str | None
        groupList: list[ActAutoChessModeGroupType]

    class ActAutoChessBondInfo(BaseStruct):
        bondId: str
        name: str
        desc: str
        iconId: str
        activeCount: int
        activeCondition: ActAutoChessBondActiveConditionType
        activeConditionTemplate: str | None
        activeParamList: list[str]
        effectId: str
        activeType: ActAutoChessBondActiveType
        identifier: int
        weight: int
        isActiveInDeck: bool
        maxInactiveBondCount: int
        noStack: bool
        noSelect: bool
        chessIdList: list[str]

    class ActAutoChessGarrisonData(BaseStruct):
        garrisonDesc: str | None
        eventType: str
        eventTypeDesc: str
        eventTypeIcon: str
        eventTypeSmallIcon: str
        eventEffect: str | None
        effectType: str
        charLevel: int
        battleRuneKey: str | None
        blackboard: "list[Blackboard]"
        description: str | None

    class ActAutoChessBandData(BaseStruct):
        bandId: str
        sortId: int
        bandType: AutoChessBandType
        inactiveModeIdList: list[str]
        bandDesc: str
        totalHp: int
        effectId: str
        victorCount: int
        masterVictorCount: int
        bandRewardModulus: float
        offseasonPriority: int
        relateBondList: list[str] | None

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
        equipSlotNum: int
        showTag: str | None
        bondIds: list[str]
        garrisonIds: list[str] | None
        desc: str | None

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
        canGiveBond: bool
        canFuse: bool
        fuseWith: str | None
        fuseResult: str | None
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
        showTag: str | None
        displayInHUD: bool

    class ActAutoChessBuffInfoData(BaseStruct):
        key: str
        blackboard: "list[Blackboard]"

    class ActAutoChessEffectChoiceInfoData(BaseStruct):
        choiceEventId: str
        choiceType: AutoChessEffectChoiceType
        effectType: AutoChessEffectType
        selectionType: AutoChessSelectionType
        name: str
        desc: str

    class ActAutoChessPlayerTitleData(BaseStruct):
        id: str
        type: str
        point: int
        rank: int
        picId: str
        txt: str

    class ActAutochessBossEntry(BaseStruct):
        bossId: str
        sortId: int
        weight: int
        bloodDataDict: dict[str, int]
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
        countSingle: int
        weight: int
        showEnemyId: str

    class ActAutoChessTrainingNpcData(BaseStruct):
        npcId: str
        charId: str
        nameCardSkinId: str
        medalCount: int
        bandId: str

    class ActAutoChessConstData(BaseStruct):
        shopRefreshPrice: int
        maxDeckChessCnt: int
        maxDeckEquipmentChessCnt: int
        maxBattleChessCnt: int
        fallbackBondId: str | None
        storeCntMax: int
        costPlayerHpLimit: int
        borrowCount: int
        milestoneId: str | None
        dailyMissionParam: int
        dailyMissionName: str | None
        dailyMissionRule: str | None
        milestoneTrackId: str | None
        escapedBattleTemplateMapSinglePlayer: str | None
        escapedBattleTemplateMapMultiPlayer: str | None
        webBusType: str | None
        webUpdateLogBusType: str | None
        itemMaxCount: int
        diyCharLimitForLevels: dict[str, int] | None
        permShopLogoId: str | None
        contentUpdateTime: int
        systemCustomChar: list[str] | None
        bossIconId: str | None
        modeWarningDiff: int
        perfectBattleVoiceRound: int
        loseHpVoiceRound: int
        bondVoiceLayers: list[int]
        shopTagWarmUpId: str | None

    class ActAutoChessEffectDescParamData(BaseStruct):
        descParamInfos: "list[ActAutoChessData.ActAutoChessEffectDescParamInfo]"
        phaseType: ActAutoChessBondPhaseType
        bondPhaseCountList: list[int]

    class ActAutoChessEffectDescParamInfo(BaseStruct):
        descParamBase: str
        descParamPerStack: str
        descParamMax: float

    class ActAutoChessModeGroupData(BaseStruct):
        groupType: ActAutoChessModeGroupType
        modeType: ActAutoChessMultiModeSubType
        willExpand: bool
        modeIds: list[str]

    class ActAutoChessSkillInfoData(BaseStruct):
        effectId: str
        skillDesc: str
        skillType: AutoChessSkillType
        skillCost: int
        skillAvailType: AutoChessSkillAvailType
        skillAvailCount: int
        unlockType: str
        unlockParam: list[str]
        minorUnlock: bool
        unlockEffectId: str | None
        targetType: str | None
        targetFilterType: str | None
        targetTip: str | None
        isUnusableAtSpecialRecruit: bool
        bandId: str


class ActAutoChessTrainingData(BaseStruct):
    overrideAutoChessData: "ActAutoChessTrainingData.AutoChessTrainingData"
    bandDataListDict: dict[str, ActAutoChessData.ActAutoChessBandData]
    bondInfoDict: dict[str, ActAutoChessData.ActAutoChessBondInfo]
    garrisonDataDict: dict[str, ActAutoChessData.ActAutoChessGarrisonData]
    effectInfoDataDict: dict[str, ActAutoChessData.ActAutoChessEffectInfoData]
    effectDescParamDataDict: dict[str, ActAutoChessData.ActAutoChessEffectDescParamData]
    skillInfoDataDict: dict[str, ActAutoChessData.ActAutoChessSkillInfoData]
    effectBuffInfoDataDict: dict[str, list[ActAutoChessData.ActAutoChessBuffInfoData]]
    shopLevelDataDict: dict[str, dict[str, ActAutoChessData.ActAutoChessShopLevelData]]
    charChessDataDict: dict[str, ActAutoChessData.ActAutoChessCharChessData]
    charShopChessDatas: dict[str, ActAutoChessData.ActAutoChessCharShopChessData]
    trapChessDataDict: dict[str, ActAutoChessData.ActAutoChessTrapChessData]
    trapShopChessDatas: dict[str, ActAutoChessData.ActAutoChessTrapShopChessData]
    chessNormalIdLookupDict: dict[str, str]
    effectChoiceInfoDict: dict[str, ActAutoChessData.ActAutoChessEffectChoiceInfoData]
    battleDataDict: dict[str, dict[str, list[ActAutoChessData.ActAutoChessBattleData]]]
    bossInfoDict: dict[str, ActAutoChessData.ActAutochessBossEntry]
    specialEnemyInfoDict: dict[str, ActAutoChessData.ActAutochessSpecialEnemyEntry]
    trainingNpcList: list[ActAutoChessData.ActAutoChessTrainingNpcData]
    constData: ActAutoChessData.ActAutoChessConstData
    trainingConstData: "ActAutoChessTrainingData.TrainingConstData"
    trainingShopDict: dict[str, "list[ActAutoChessTrainingData.TrainingShopSlotData]"]
    trainingRoundInfoDict: dict[str, "ActAutoChessTrainingData.TrainingRoundInfoData"]
    trainingSpecialChoiceDict: dict[str, "list[ActAutoChessTrainingData.TrainingSpecialChoiceData]"]
    trainingNpcDeployDict: dict[str, "list[ActAutoChessTrainingData.TrainingNpcDeployData]"]
    trainingDiyChessDict: dict[str, "ActAutoChessTrainingData.TrainingDiyChessData"]
    specialEnemyRandomTypeDict: dict[str, ActAutoChessData.ActAutochessSpecialEnemyTypeEntry]

    class AutoChessTrainingData(BaseStruct):
        bandDataDict: dict[str, AutoChessData.AutoChessBandData]
        bondDataDict: dict[str, AutoChessData.AutoChessBondInfoData]
        bossInfoDict: dict[str, AutoChessData.AutoChessBossInfoData]
        randomEnemyAttributeDict: dict[str, AutoChessData.AutoChessRandomEnemyAttributeData]

    class TrainingConstData(BaseStruct):
        trstageBandId: str
        trstageBossId: str
        trStageId: str
        trainingModeId: str
        trSpecialEnemyTypes: list[str]
        trBondIds: list[str]
        trBannedBondIds: list[str]
        trStageBossHP: int
        trInGameDiyChessId: str
        trInGameBanDiyChessId: str

    class TrainingDiyChessData(BaseStruct):
        chessId: str
        charId: str
        tmplId: str | None
        skinId: str
        skillIndex: int
        uniEquipId: str | None
        potentialRank: int

    class TrainingNpcDeployData(BaseStruct):
        round: int
        trainingNpcId: str
        chessId: str
        position: Vector2
        direction: int
        equipChessIds: list[str] | None
        garrisonLayer: int

    class TrainingRoundInfoData(BaseStruct):
        round: int
        isBossTurn: bool
        baseGoldCnt: int

    class TrainingShopSlotData(BaseStruct):
        slot: int
        chessIds: list[str]

    class TrainingSpecialChoiceData(BaseStruct):
        choiceEventId: str
        round: int
        slot: int
        equipId: str
        trainingNpcId: str | None
