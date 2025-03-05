from .item_bundle import ItemBundle
from ..common import BaseStruct, CustomIntEnum


class Act35SideData(BaseStruct):
    class Act35SideDialogueType(CustomIntEnum):
        NONE = "NONE", 0
        ENTRY = "ENTRY", 1
        BONUS = "BONUS", 2
        BUY = "BUY", 3
        PROCESS = "PROCESS", 4

    class Act35SideDialogueNameBgType(CustomIntEnum):
        NONE = "NONE", 0
        GREEN = "GREEN", 1
        BLUE = "BLUE", 2

    challengeDataMap: dict[str, "Act35SideData.Act35SideChallengeData"]
    roundDataMap: dict[str, "Act35SideData.Act35SideRoundData"]
    taskDataMap: dict[str, "Act35SideData.Act35SideChallengeTaskData"]
    cardDataMap: dict[str, "Act35SideData.Act35SideCardData"]
    materialDataMap: dict[str, "Act35SideData.Act35SideMaterialData"]
    dialogueGroupDataMap: dict[str, "Act35SideData.Act35SideDialogueGroupData"]
    constData: "Act35SideData.Act35SideConstData"
    mileStoneList: list["Act35SideData.Act35SideMileStoneData"]
    zoneAdditionDataMap: dict[str, "Act35SideData.Act35SideZoneAdditionData"]

    class Act35SideChallengeData(BaseStruct):
        challengeId: str
        challengeName: str
        challengeDesc: str
        sortId: int
        challengePicId: str
        challengeIconId: str
        openTime: int
        preposedChallengeId: str | None
        passRound: int
        passRoundScore: int
        roundIdList: list[str]

    class Act35SideRoundData(BaseStruct):
        roundId: str
        challengeId: str
        round: int
        roundPassRating: int
        isMaterialRandom: bool
        fixedMaterialList: dict[str, int] | None
        passRoundCoin: int

    class Act35SideChallengeTaskData(BaseStruct):
        taskId: str
        taskDesc: str
        materialId: str
        materialNum: int
        passTaskCoin: int

    class Act35SideCardData(BaseStruct):
        cardId: str
        sortId: int
        rank: int
        cardFace: str
        cardPic: str
        levelDataList: list["Act35SideData.Act35SideCardLevelData"]

    class Act35SideCardLevelData(BaseStruct):
        cardLevel: int
        cardName: str
        cardDesc: str
        inputMaterialList: list["Act35SideData.Act35SideCardMaterialData"]
        outputMaterialList: list["Act35SideData.Act35SideCardMaterialData"]

    class Act35SideCardMaterialData(BaseStruct):
        materialId: str
        count: int

    class Act35SideMaterialData(BaseStruct):
        materialId: str
        sortId: int
        materialIcon: str
        materialName: str
        materialRating: int

    class Act35SideDialogueGroupData(BaseStruct):
        type: "Act35SideData.Act35SideDialogueType"
        dialogDataList: list["Act35SideData.Act35SideDialogueData"]

    class Act35SideDialogueData(BaseStruct):
        sortId: int
        iconId: str
        name: str
        content: str
        bgType: "Act35SideData.Act35SideDialogueNameBgType"

    class Act35SideConstData(BaseStruct):
        campaignStageId: str
        campaignEnemyCnt: int
        milestoneGrandRewardInfoList: list["Act35SideData.Act35SideMileStoneGrandRewardInfo"]
        unlockLevelId: str
        birdSpineLowRate: float
        birdSpineHighRate: float
        cardMaxLevel: int
        maxSlotCnt: int
        cardRefreshNum: int
        initSlotCnt: int
        bonusMaterialId: str
        introRoundIdList: list[str]
        challengeUnlockText: str
        slotUnlockText: str
        estimateRatio: int
        carvingUnlockToastText: str

    class Act35SideMileStoneGrandRewardInfo(BaseStruct):
        itemName: str
        level: int

    class Act35SideMileStoneData(BaseStruct):
        mileStoneId: str
        mileStoneLvl: int
        needPointCnt: int
        rewardItem: ItemBundle

    class Act35SideZoneAdditionData(BaseStruct):
        zoneId: str
        unlockText: str
