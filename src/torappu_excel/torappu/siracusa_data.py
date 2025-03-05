from enum import StrEnum

from .item_bundle import ItemBundle
from ..common import BaseStruct

from msgspec import field


class SiracusaData(BaseStruct):
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

    class AreaData(BaseStruct):
        areaId: str
        areaName: str
        areaSubName: str
        unlockType: "SiracusaData.ZoneUnlockType"
        unlockStage: str | None
        areaIconId: str
        pointList: list[str]

    class PointData(BaseStruct):
        pointId: str
        areaId: str
        pointName: str
        pointDesc: str
        pointIconId: str
        pointItaName: str

    class CharCardData(BaseStruct):
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
        gainType: "SiracusaData.CardGainType | None" = field(default=None)

    class TaskRingData(BaseStruct):
        taskRingId: str
        sortIndex: int
        charCardId: str
        logicType: "SiracusaData.TaskRingLogicType"
        ringText: str
        item: ItemBundle
        isPrecious: bool
        taskIdList: list[str]

    class TaskBasicInfoData(BaseStruct):
        taskId: str
        taskRingId: str
        sortIndex: int
        placeId: str
        npcId: str | None
        taskType: "SiracusaData.TaskType"

    class BattleTaskData(BaseStruct):
        taskId: str
        stageId: str
        battleTaskDesc: str
        targetType: str | None = field(default=None)
        targetTemplate: str | None = field(default=None)
        targetParamList: list[str] | None = field(default=None)

    class AVGTaskData(BaseStruct):
        taskId: str
        taskAvg: str

    class ItemInfoData(BaseStruct):
        itemId: str
        itemName: str
        itemItalyName: str
        itemDesc: str
        itemIcon: str

    class ItemCardInfoData(BaseStruct):
        cardId: str
        cardName: str
        cardDesc: str
        optionScript: str

    class NavigationInfoData(BaseStruct):
        entryId: str
        navigationType: "SiracusaData.NavigationType"
        entryIcon: str
        entryName: str | None
        entrySubName: str | None

    class OptionInfoData(BaseStruct):
        optionId: str
        optionDesc: str
        optionScript: str
        optionGoToScript: str | None
        isLeaveOption: bool
        needCommentLike: bool
        requireCardId: str | None

    class StagePointInfoData(BaseStruct):
        stageId: str
        pointId: str
        sortId: int
        isTaskStage: bool

    class StoryBriefInfoData(BaseStruct):
        storyId: str
        stageId: str
        storyInfo: str

    class OperaInfoData(BaseStruct):
        operaId: str
        sortId: int
        operaName: str
        operaSubName: str
        operaScore: str
        unlockTime: int

    class OperaCommentInfoData(BaseStruct):
        commentId: str
        referenceOperaId: str
        columnIndex: int
        columnSortId: int
        commentTitle: str
        score: str
        commentContent: str
        commentCharId: str

    class ConstData(BaseStruct):
        operaDailyNum: int
        operaAllUnlockTime: int
        defaultFocusArea: str
