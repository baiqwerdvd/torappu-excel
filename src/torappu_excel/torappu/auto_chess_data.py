from .auto_chess_bond_type import AutoChessBondType
from .auto_chess_broadcast_type import AutoChessBroadcastType
from .auto_chess_prepare_step_type import AutoChessPrepareStepType
from .auto_chess_shop_token_display_type import AutoChessShopTokenDisplayType
from .auto_chess_skill_trigger_type import AutoChessSkillTriggerType
from .blackboard import Blackboard
from .common_report_player_data import CommonReportPlayerData
from .evolve_phase import EvolvePhase
from .ping_cond import PingCond
from .profession_category import ProfessionCategory
from ..common import BaseStruct


class AutoChessData(BaseStruct):
    versionInfoDict: dict[str, "AutoChessData.AutoChessVersionInfoData"]
    bandDataDict: dict[str, "AutoChessData.AutoChessBandData"]
    cultivateEffectList: "list[AutoChessData.AutoChessCultivateRelationData]"
    effectTypeDataDict: dict[str, "AutoChessData.AutoChessEffectTypeData"]
    bondInfoDict: dict[str, "AutoChessData.AutoChessBondInfoData"]
    bossInfoDict: dict[str, "AutoChessData.AutoChessBossInfoData"]
    enemyTypeDatas: dict[str, "AutoChessData.AutoChessEnemyTypeData"]
    enterStepList: "list[AutoChessData.AutoChessEnterStepData]"
    shopStateTokenDict: dict[str, "AutoChessData.AutoChessShopStateTokenData"]
    skillTriggerDataList: "list[AutoChessData.AutoChessSkillTriggerData]"
    skillRangeDict: dict[str, str]
    prepareStateDict: dict[str, "AutoChessData.AutoChessPrepareStateData"]
    randomEnemyAttributeDict: dict[str, "AutoChessData.AutoChessRandomEnemyAttributeData"]
    enabledEmoticonThemeIdList: list[str]
    gameTipsList: "list[AutoChessData.AutoChessGameTipData]"
    medalDataList: "list[AutoChessData.AutoChessMedalData]"
    turnInfoDataDict: dict[str, dict[str, "AutoChessData.AutoChessTurnInfoData"]]
    roundScoreDataList: "list[AutoChessData.AutoChessRoundScoreData]"
    reportPlayerDataList: list[CommonReportPlayerData]
    broadcastList: "list[AutoChessData.AutoChessBroadcastData]"
    constData: "AutoChessData.AutoChessConstData"

    class AutoChessVersionInfoData(BaseStruct):
        versionId: str | None
        activityId: str
        updateTime: int
        appearTimeOnMainScreen: int
        disappearTimeOnMainScreen: int

    class AutoChessBandData(BaseStruct):
        bandId: str
        bandName: str
        bandIconId: str
        unlockDesc: str | None

    class AutoChessBroadcastData(BaseStruct):
        id: str
        desc: str
        priority: int
        type: AutoChessBroadcastType
        paramList: list[str]

    class AutoChessCultivateRelationData(BaseStruct):
        cultivateNum: int
        effectId: str
        evolvePhase: EvolvePhase
        charLevel: int
        atkPer: int
        defPer: int
        hpPer: int

    class AutoChessEffectTypeData(BaseStruct):
        description: str | None

    class AutoChessBondInfoData(BaseStruct):
        bondId: str
        bondType: AutoChessBondType
        powerIdList: list[str]
        name: str
        icon: str
        isPower: bool
        bondOrder: int

    class AutoChessBossInfoData(BaseStruct):
        bossId: str
        enemyId: str
        handbookEnemyId: str

    class AutoChessEnemyTypeData(BaseStruct):
        type: str
        sortId: int
        name: str
        description: str
        icon: str
        typeIdentifier: int
        involveRandom: bool

    class AutoChessEnterStepData(BaseStruct):
        stepType: AutoChessPrepareStepType
        sortId: int
        time: int
        hintTime: int
        title: str
        desc: str | None

    class AutoChessShopStateTokenData(BaseStruct):
        tokenId: str
        tokenDisplayType: AutoChessShopTokenDisplayType

    class AutoChessSkillTriggerData(BaseStruct):
        profession: ProfessionCategory
        subProfessionId: str | None
        charId: str | None
        skillIndex: int
        skillTriggerType: AutoChessSkillTriggerType

    class AutoChessPrepareStateData(BaseStruct):
        effectId: str
        buff: str | None
        blackBoard: "list[Blackboard]"

    class AutoChessRandomEnemyAttributeData(BaseStruct):
        enemyKey: str
        level: int
        extraEnemyIdentifier: int
        extraEnemyKeyList: list[str] | None
        isFlyEnemy: bool
        enemyBattleEffectivenessFactor: float

    class AutoChessConstData(BaseStruct):
        pingConds: list[PingCond]
        matchingTipRotateInterval: float
        minReplacedEnemyCount: int
        maxReplacedEnemyCount: int
        templateEnemyNormal: str
        templateEnemyElite: str
        templateEnemySpecial: str
        templateEnemyNormalFly: str
        templateEnemyEliteFly: str
        templateEnemySpecialFly: str
        templateEnemyToken: str
        templateEnemyTokenFly: str
        maxLevelCnt: int
        specialEnemyNum: int
        enemyTypeIdentifierToFillRandom: int
        enemyMaxHpFactor: float
        enemyAtkFactor: float
        enemyDefFactor: float
        enemyMagicResistanceFactor: float
        specialPhaseStayTime: int
        hintTimeSpecialPhase: int
        hintTimeNormalPhase: int
        hintTimeFightPhase: int
        hintTimeDotPhase: int
        invitationSendCd: int
        discountColor: str
        premiumColor: str
        normalColor: str
        reportMaxNum: int
        chatCD: float
        chatTime: float
        broadcastBeginDelay: float
        noMoneyTipsBand: list[str]
        bossTrailerStartRound: int
        singleClosureStayTime: float
        matchTimeMax: float

    class AutoChessTurnInfoData(BaseStruct):
        round: int
        normalPhaseTime: int
        isBossTurn: bool
        bossTurnHpReduceTime: int

    class AutoChessMedalData(BaseStruct):
        medalCount: int
        medalIconId: str

    class AutoChessGameTipData(BaseStruct):
        tip: str
        weight: int

    class AutoChessRoundScoreData(BaseStruct):
        round: int
        score: int
