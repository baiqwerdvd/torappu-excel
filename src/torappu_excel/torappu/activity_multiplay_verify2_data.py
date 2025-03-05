from enum import StrEnum

from .evolve_phase import EvolvePhase
from .item_bundle import ItemBundle
from .player_avatar_group_type import PlayerAvatarGroupType
from ..common import BaseStruct

from msgspec import field


class ActivityMultiplayVerify2Data(BaseStruct):
    class Act2VMultiRoomStepType(StrEnum):
        NONE = "NONE"
        STAGE_CHOOSE = "STAGE_CHOOSE"
        ENTRANCE = "ENTRANCE"
        CHAR_PICK = "CHAR_PICK"
        SYS_ALLOC = "SYS_ALLOC"
        SQUAD_CHECK = "SQUAD_CHECK"

    class Act2VMultiIdentityType(StrEnum):
        NONE = "NONE"
        HIGH = "HIGH"
        LOW = "LOW"
        TEMPORARY = "TEMPORARY"
        ALL = "ALL"

    class Act2VMultiMapType(StrEnum):
        NORMAL = "NORMAL"
        FOOTBALL = "FOOTBALL"
        DEFENCE = "DEFENCE"

    class Act2VMultiMapDifficultyType(StrEnum):
        TRAINING = "TRAINING"
        ORDINARY = "ORDINARY"
        DIFFICULTY = "DIFFICULTY"

    class Act2VMultiEmojiChatSceneType(StrEnum):
        NONE = "NONE"
        ROOM = "ROOM"
        PICK = "PICK"

    selectStepDataList: list["ActivityMultiplayVerify2Data.Act2VMultiSelectStepData"]
    identityDataList: list["ActivityMultiplayVerify2Data.Act2VMultiIdentityData"]
    mapTypeDatas: dict[str, "ActivityMultiplayVerify2Data.Act2VMultiMapTypeData"]
    mapDatas: dict[str, "ActivityMultiplayVerify2Data.Act2VMultiMapData"]
    targetMissionDatas: dict[str, "ActivityMultiplayVerify2Data.Act2VMultiTargetMissionData"]
    mileStoneList: list["ActivityMultiplayVerify2Data.Act2VMultiMilestoneData"]
    stageStarRewardDatas: dict[str, "ActivityMultiplayVerify2Data.Act2VMultiStageStarRewardData"]
    emojiChatDatas: dict[str, "ActivityMultiplayVerify2Data.Act2VMultiEmojiChatData"]
    commentDatas: dict[str, "ActivityMultiplayVerify2Data.Act2VMultiCommentData"]
    tipsDataList: list["ActivityMultiplayVerify2Data.Act2VMultiTipsData"]
    reportDataList: list["ActivityMultiplayVerify2Data.Act2VMultiReportData"]
    tempCharDataList: list["ActivityMultiplayVerify2Data.Act2VMultiTempCharData"]
    constData: "ActivityMultiplayVerify2Data.Act2VMultiConstData"
    constToastData: "ActivityMultiplayVerify2Data.Act2VMultiConstToastData"
    mapTypeNameDataList: list["ActivityMultiplayVerify2Data.Act2VMultiMapTypeNameData"]
    difficultyNameDataList: list["ActivityMultiplayVerify2Data.Act2VMultiMapDifficultyNameData"]
    buffIconDatas: dict[str, "ActivityMultiplayVerify2Data.Act2VMultiBuffIconData"]

    class Act2VMultiSelectStepData(BaseStruct):
        stepType: "ActivityMultiplayVerify2Data.Act2VMultiRoomStepType"
        sortId: int
        time: int
        hintTime: int
        title: str
        desc: str | None

    class Act2VMultiIdentityData(BaseStruct):
        id_: str = field(name="id")
        sortId: int
        picId: str
        type_: "ActivityMultiplayVerify2Data.Act2VMultiIdentityType" = field(name="type")
        maxNum: int
        color: str | None

    class Act2VMultiMapTypeData(BaseStruct):
        type_: "ActivityMultiplayVerify2Data.Act2VMultiMapType" = field(name="type")
        difficulty: "ActivityMultiplayVerify2Data.Act2VMultiMapDifficultyType"
        squadMax: int
        matchUnlockModeId: str | None
        matchUnlockParam: int
        stageIdInModeList: list[str]
        modeIconId: str

    class Act2VMultiMapData(BaseStruct):
        stageId: str
        modeId: str
        sortId: int
        missionIdList: list[str]
        stageSmallPreviewId: str
        stageBigPreviewId: str
        displayEnemyIdList: list[str]

    class Act2VMultiTargetMissionData(BaseStruct):
        id_: str = field(name="id")
        sortId: int
        title: str
        battleDesc: str
        description: str
        starNum: int

    class Act2VMultiMilestoneData(BaseStruct):
        mileStoneId: str
        mileStoneLvl: int
        needPointCnt: int
        rewardItem: ItemBundle

    class Act2VMultiStarRewardData(BaseStruct):
        starNum: int
        rewards: list[ItemBundle]
        dailyMissionPoint: int

    class Act2VMultiStageStarRewardData(BaseStruct):
        starRewardDatas: list["ActivityMultiplayVerify2Data.Act2VMultiStarRewardData"]

    class Act2VMultiEmojiChatData(BaseStruct):
        id_: str = field(name="id")
        type_: "ActivityMultiplayVerify2Data.Act2VMultiEmojiChatSceneType" = field(name="type")
        sortId: int
        picId: str
        desc: str

    class Act2VMultiCommentData(BaseStruct):
        id_: str = field(name="id")
        type_: "ActivityMultiplayVerify2Data.Act2VMultiMapType" = field(name="type")
        priorityId: int
        picId: str
        txt: str
        template: str
        paramList: list[str]

    class Act2VMultiTipsData(BaseStruct):
        id_: str = field(name="id")
        txt: str
        weight: int

    class Act2VMultiReportData(BaseStruct):
        id_: str = field(name="id")
        sortId: int
        txt: str
        desc: str

    class Act2VMultiTempCharData(BaseStruct):
        charId: str
        level: int
        evolvePhase: EvolvePhase
        mainSkillLevel: int
        specializeLevel: int
        potentialRank: int
        favorPoint: int
        skinId: str

    class Act2VMultiConstDataPingCond(BaseStruct):
        cond: int
        txt: str

    class Act2VMultiConstData(BaseStruct):
        milestoneId: str
        maxUnlockNum: int
        roomNumCopyDesc: str
        noMapRoomNumCopyDesc: str
        randomMapRoomNumCopyDesc: str
        targetCd: int
        squadMinNum: int
        squadMaxNum: int
        defenseTraMax: int
        defenseOrdMax: int
        defenseDifMax: int
        stageChooseAnimRandomStageIdList: list[str]
        mapUnlockDesc1: str
        mapUnlockDesc2: str
        mapUnlockDesc3: str
        mapUnlockDesc4: str
        mapUnlockDesc5: str
        mapUnlockDesc6: str
        mapUnlockDesc7: str
        difUnlockCond: int
        ordRewardStageId: str
        difRewardStageId: str
        maxMatchTime: int
        tipsSwitchTime: float
        pingConds: list["ActivityMultiplayVerify2Data.Act2VMultiConstDataPingCond"]
        chatCd: int
        chatTime: int
        markCd: int
        markCond1: int
        markCond2: int
        dailyMissionParam: int
        dailyMissionName: str
        dailyMissionDesc: str
        dailyMissionRule: str
        missionDesc: str
        dailyMissionRewardItem: ItemBundle
        normalGreatVoiceStar: int
        footballGreatVoiceNum: int
        defenceGreatVoiceWave: int
        reportMaxNum: int
        reportText: str
        rewardCardId: str
        rewardCardText: str
        rewardSkinId: str
        rewardSkinText: str
        maxRetryTimeInTeamRoom: int
        maxRetryTimeInMatchRoom: int
        maxRetryTimeInBattle: int
        maxOperatorDelay: float
        maxPlaySpeed: int
        delayTimeNeedTip: int
        settleRetryTime: int
        modeNormalUnlockModeId: str
        modeNormalUnlockParam: int
        modeDefenceUnlockModeId: str
        modeDefenceUnlockParam: int
        modeFootballUnlockModeId: str
        modeFootballUnlockParam: int
        tutorialEntryStoryId: str
        tutorialSquadStoryId: str
        teamUnlockStageId: str
        teamUnlockParam: int
        trainPartnerCharId: str
        trainPartnerCharSkinId: str
        trainPartnerPlayerName: str
        trainPartnerPlayerLevel: int
        trainPartnerBuffId: str
        trainPartnerAvatarGroupType: PlayerAvatarGroupType
        trainPartnerAvatarId: str

    class Act2VMultiConstToastData(BaseStruct):
        noRoom: str
        fullRoom: str
        roomIdFormatError: str
        roomIdCopySuccess: str
        banned: str
        serverOverload: str
        matchAliveFailed: str
        createRoomAliveFailed: str
        joinRoomAliveFailed: str
        roomOwnerReviseTarget: str
        roomCollaboratorReviseTarget: str
        roomOwnerReviseMap: str
        roomCollaboratorReviseMap: str
        roomCollaboratorJoinRoom: str
        roomCollaboratorExitRoom: str
        continuousClicks: str
        matchNoProject: str
        reportNoProject: str
        otherModeTrainingLock: str
        teamLock: str
        mentorLockTips: str
        unlockNewModeInMatch: str
        unlockNewStageInTeam: str
        unlockMentorInMatch: str
        teamFullLow: str
        teamFullHigh: str
        difficultUnlock: str

    class Act2VMultiMapTypeNameData(BaseStruct):
        mapType: "ActivityMultiplayVerify2Data.Act2VMultiMapType"
        typeName: str

    class Act2VMultiMapDifficultyNameData(BaseStruct):
        difficulty: "ActivityMultiplayVerify2Data.Act2VMultiMapDifficultyType"
        difficultyName: str

    class Act2VMultiBuffIconData(BaseStruct):
        buffId: str
        iconId: str
