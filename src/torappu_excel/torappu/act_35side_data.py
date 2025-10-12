from pydantic import BaseModel, ConfigDict

from torappu_excel.common import CustomIntEnum

from .item_bundle import ItemBundle


class Act35SideData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class Act35SideChallengeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class Act35SideRoundData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        roundId: str
        challengeId: str
        round: int
        roundPassRating: int
        isMaterialRandom: bool
        fixedMaterialList: dict[str, int] | None
        passRoundCoin: int

    class Act35SideChallengeTaskData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        taskId: str
        taskDesc: str
        materialId: str
        materialNum: int
        passTaskCoin: int

    class Act35SideCardData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        cardId: str
        sortId: int
        rank: int
        cardFace: str
        cardPic: str
        levelDataList: list["Act35SideData.Act35SideCardLevelData"]

    class Act35SideCardLevelData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        cardLevel: int
        cardName: str
        cardDesc: str
        inputMaterialList: list["Act35SideData.Act35SideCardMaterialData"]
        outputMaterialList: list["Act35SideData.Act35SideCardMaterialData"]

    class Act35SideCardMaterialData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        materialId: str
        count: int

    class Act35SideMaterialData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        materialId: str
        sortId: int
        materialIcon: str
        materialName: str
        materialRating: int

    class Act35SideDialogueGroupData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        type: "Act35SideData.Act35SideDialogueType"
        dialogDataList: list["Act35SideData.Act35SideDialogueData"]

    class Act35SideDialogueData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        sortId: int
        iconId: str
        name: str
        content: str
        bgType: "Act35SideData.Act35SideDialogueNameBgType"

    class Act35SideConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class Act35SideMileStoneGrandRewardInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemName: str
        level: int

    class Act35SideMileStoneData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        mileStoneId: str
        mileStoneLvl: int
        needPointCnt: int
        rewardItem: ItemBundle

    class Act35SideZoneAdditionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneId: str
        unlockText: str
