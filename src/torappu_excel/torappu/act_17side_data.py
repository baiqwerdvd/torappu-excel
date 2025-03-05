from enum import StrEnum

from .act_archive_type import ActArchiveType
from .item_bundle import ItemBundle
from .rune_table import RuneTable
from ..common import BaseStruct

from msgspec import field


class Act17sideData(BaseStruct):
    class NodeType(StrEnum):
        LANDMARK = "LANDMARK"
        STORY = "STORY"
        BATTLE = "BATTLE"
        ENDING = "ENDING"
        TREASURE = "TREASURE"
        EVENT = "EVENT"
        TECH = "TECH"
        CHOICE = "CHOICE"

    class TreasureType(StrEnum):
        SMALL = "SMALL"
        SPECIAL = "SPECIAL"

    class TrackPointType(StrEnum):
        NONE = "NONE"
        MAIN = "MAIN"
        SUB = "SUB"

    class ArchiveItemUnlockCondition(StrEnum):
        NONE = "NONE"
        STAGE = "STAGE"
        NODE = "NODE"

    class ArchiveItemStageUnlockParam(StrEnum):
        NONE = "NONE"
        PLAYED = "PLAYED"
        PASS = "PASS"
        COMPLETE = "COMPLETE"

    class ChapterIconType(StrEnum):
        NONE = "NONE"
        NORMAL = "NORMAL"
        EX = "EX"
        HARD = "HARD"

    placeDataMap: dict[str, "Act17sideData.PlaceData"]
    nodeInfoDataMap: dict[str, "Act17sideData.NodeInfoData"]
    landmarkNodeDataMap: dict[str, "Act17sideData.LandmarkNodeData"]
    storyNodeDataMap: dict[str, "Act17sideData.StoryNodeData"]
    battleNodeDataMap: dict[str, "Act17sideData.BattleNodeData"]
    treasureNodeDataMap: dict[str, "Act17sideData.TreasureNodeData"]
    eventNodeDataMap: dict[str, "Act17sideData.EventNodeData"]
    techNodeDataMap: dict[str, "Act17sideData.TechNodeData"]
    choiceNodeDataMap: dict[str, "Act17sideData.ChoiceNodeData"]
    eventDataMap: dict[str, "Act17sideData.EventData"]
    archiveItemUnlockDataMap: dict[str, "Act17sideData.ArchiveItemUnlockData"]
    techTreeDataMap: dict[str, "Act17sideData.TechTreeData"]
    techTreeBranchDataMap: dict[str, "Act17sideData.TechTreeBranchData"]
    mainlineChapterDataMap: dict[str, "Act17sideData.MainlineChapterData"]
    mainlineDataMap: dict[str, "Act17sideData.MainlineData"]
    zoneDataList: list["Act17sideData.ZoneData"]
    constData: "Act17sideData.ConstData"

    class PlaceData(BaseStruct):
        placeId: str
        placeDesc: str
        lockEventId: str | None
        zoneId: str
        visibleCondType: str | None = field(default=None)
        visibleParams: list[str] | None = field(default=None)

    class NodeInfoData(BaseStruct):
        nodeId: str
        nodeType: "Act17sideData.NodeType"
        sortId: int
        placeId: str
        isPointPlace: bool
        chapterId: str
        trackPointType: "Act17sideData.TrackPointType"
        unlockCondType: str | None = field(default=None)
        unlockParams: list[str] | None = field(default=None)

    class LandmarkNodeData(BaseStruct):
        nodeId: str
        landmarkId: str
        landmarkName: str
        landmarkPic: str | None
        landmarkSpecialPic: str
        landmarkDesList: list[str]

    class StoryNodeData(BaseStruct):
        nodeId: str
        storyId: str
        storyKey: str
        storyName: str
        storyPic: str | None
        confirmDes: str
        storyDesList: list[str]

    class BattleNodeData(BaseStruct):
        nodeId: str
        stageId: str

    class TreasureNodeData(BaseStruct):
        nodeId: str
        treasureId: str
        treasureName: str
        treasurePic: str | None
        treasureSpecialPic: str | None
        endEventId: str
        confirmDes: str
        treasureDesList: list[str]
        missionIdList: list[str]
        rewardList: list[ItemBundle]
        treasureType: "Act17sideData.TreasureType"

    class EventNodeData(BaseStruct):
        nodeId: str
        eventId: str
        endEventId: str

    class TechNodeData(BaseStruct):
        nodeId: str
        techTreeId: str
        techTreeName: str
        techPic: str | None
        techSpecialPic: str
        endEventId: str
        confirmDes: str
        techDesList: list[str]
        missionIdList: list[str]

    class ChoiceNodeOptionData(BaseStruct):
        canRepeat: bool
        eventId: str
        des: str
        unlockDes: str | None
        unlockCondType: str | None = field(default=None)
        unlockParams: list[str] | None = field(default=None)

    class ChoiceNodeData(BaseStruct):
        nodeId: str
        choicePic: str | None
        isDisposable: bool
        choiceSpecialPic: str | None
        choiceName: str
        choiceDesList: list[str]
        cancelDes: str
        choiceNum: int
        optionList: list["Act17sideData.ChoiceNodeOptionData"]

    class EventData(BaseStruct):
        eventId: str
        eventPic: str | None
        eventSpecialPic: str | None
        eventTitle: str
        eventDesList: list[str]

    class ArchiveItemUnlockData(BaseStruct):
        itemId: str
        itemType: ActArchiveType
        unlockCondition: "Act17sideData.ArchiveItemUnlockCondition"
        nodeId: str | None
        stageParam: "Act17sideData.ArchiveItemStageUnlockParam"
        chapterId: str | None

    class TechTreeData(BaseStruct):
        techTreeId: str
        sortId: int
        techTreeName: str
        defaultBranchId: str
        lockDes: str

    class TechTreeBranchData(BaseStruct):
        techTreeBranchId: str
        techTreeId: str
        techTreeBranchName: str
        techTreeBranchIcon: str
        techTreeBranchDesc: str
        runeData: RuneTable.PackedRuneData

    class MainlineChapterData(BaseStruct):
        chapterId: str
        chapterDes: str
        chapterIcon: "Act17sideData.ChapterIconType"
        unlockDes: str
        id_: str = field(name="id")

    class MainlineData(BaseStruct):
        mainlineId: str
        nodeId: str | None
        sortId: int
        missionSort: str
        zoneId: str
        mainlineDes: str
        focusNodeId: str | None

    class ZoneData(BaseStruct):
        zoneId: str
        unlockPlaceId: str | None
        unlockText: str

    class ConstData(BaseStruct):
        techTreeUnlockEventId: str
