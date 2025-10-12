from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from .item_bundle import ItemBundle


class SiracusaData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class ZoneUnlockType(StrEnum):
        NONE = "NONE"
        STAGE_UNLOCK = "STAGE_UNLOCK"
        TASK_UNLOCK = "TASK_UNLOCK"

    class CardGainType(StrEnum):
        NONE = "NONE"
        STAGE_GAIN = "STAGE_GAIN"
        TASK_GAIN = "TASK_GAIN"

    class TaskRingLogicType(StrEnum):
        NONE = "NONE"
        LINEAR = "LINEAR"
        AND = "AND"
        OR = "OR"

    class TaskType(StrEnum):
        NONE = "NONE"
        BATTLE = "BATTLE"
        AVG = "AVG"

    class NavigationType(StrEnum):
        NONE = "NONE"
        AVG = "AVG"
        LEVEL = "LEVEL"
        CHAR_CARD = "CHAR_CARD"

    areaDataMap: dict[str, "SiracusaData.AreaData"]
    pointDataMap: dict[str, "SiracusaData.PointData"]
    charCardMap: dict[str, "SiracusaData.CharCardData"]
    taskRingMap: dict[str, "SiracusaData.TaskRingData"]
    taskInfoMap: dict[str, "SiracusaData.TaskBasicInfoData"]
    battleTaskMap: dict[str, "SiracusaData.BattleTaskData"]
    avgTaskMap: dict[str, "SiracusaData.AVGTaskData"]
    itemInfoMap: dict[str, "SiracusaData.ItemInfoData"]
    itemCardInfoMap: dict[str, "SiracusaData.ItemCardInfoData"]
    navigationInfoMap: dict[str, "SiracusaData.NavigationInfoData"]
    optionInfoMap: dict[str, "SiracusaData.OptionInfoData"]
    stagePointList: list["SiracusaData.StagePointInfoData"]
    storyBriefInfoDataMap: dict[str, "SiracusaData.StoryBriefInfoData"]
    operaInfoMap: dict[str, "SiracusaData.OperaInfoData"]
    operaCommentInfoMap: dict[str, "SiracusaData.OperaCommentInfoData"]
    constData: "SiracusaData.ConstData"

    class AreaData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        areaId: str
        areaName: str
        areaSubName: str
        unlockType: "SiracusaData.ZoneUnlockType"
        unlockStage: str | None
        areaIconId: str
        pointList: list[str]

    class PointData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        pointId: str
        areaId: str
        pointName: str
        pointDesc: str
        pointIconId: str
        pointItaName: str

    class CharCardData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        charCardId: str
        sortIndex: int
        avgChar: str
        avgCharOffsetY: float | int
        charCardName: str
        charCardItaName: str
        charCardTitle: str
        charCardDesc: str
        fullCompleteDes: str
        gainDesc: str
        themeColor: str
        taskRingList: list[str]
        operaItemId: str
        gainParamList: list[str] | None
        gainType: "SiracusaData.CardGainType | None" = Field(default=None)

    class TaskRingData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        taskRingId: str
        sortIndex: int
        charCardId: str
        logicType: "SiracusaData.TaskRingLogicType"
        ringText: str
        item: ItemBundle
        isPrecious: bool
        taskIdList: list[str]

    class TaskBasicInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        taskId: str
        taskRingId: str
        sortIndex: int
        placeId: str
        npcId: str | None
        taskType: "SiracusaData.TaskType"

    class BattleTaskData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        taskId: str
        stageId: str
        battleTaskDesc: str
        targetType: str | None = Field(default=None)
        targetTemplate: str | None = Field(default=None)
        targetParamList: list[str] | None = Field(default=None)

    class AVGTaskData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        taskId: str
        taskAvg: str

    class ItemInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemId: str
        itemName: str
        itemItalyName: str
        itemDesc: str
        itemIcon: str

    class ItemCardInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        cardId: str
        cardName: str
        cardDesc: str
        optionScript: str

    class NavigationInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        entryId: str
        navigationType: "SiracusaData.NavigationType"
        entryIcon: str
        entryName: str | None
        entrySubName: str | None

    class OptionInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        optionId: str
        optionDesc: str
        optionScript: str
        optionGoToScript: str | None
        isLeaveOption: bool
        needCommentLike: bool
        requireCardId: str | None

    class StagePointInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        pointId: str
        sortId: int
        isTaskStage: bool

    class StoryBriefInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        storyId: str
        stageId: str
        storyInfo: str

    class OperaInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        operaId: str
        sortId: int
        operaName: str
        operaSubName: str
        operaScore: str
        unlockTime: int

    class OperaCommentInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        commentId: str
        referenceOperaId: str
        columnIndex: int
        columnSortId: int
        commentTitle: str
        score: str
        commentContent: str
        commentCharId: str

    class ConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        operaDailyNum: int
        operaAllUnlockTime: int
        defaultFocusArea: str
