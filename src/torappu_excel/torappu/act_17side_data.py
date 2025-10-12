from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from .act_archive_type import ActArchiveType
from .item_bundle import ItemBundle
from .rune_table import RuneTable


class Act17sideData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class PlaceData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        placeId: str
        placeDesc: str
        lockEventId: str | None
        zoneId: str
        visibleCondType: str | None = Field(default=None)
        visibleParams: list[str] | None = Field(default=None)

    class NodeInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        nodeId: str
        nodeType: "Act17sideData.NodeType"
        sortId: int
        placeId: str
        isPointPlace: bool
        chapterId: str
        trackPointType: "Act17sideData.TrackPointType"
        unlockCondType: str | None = Field(default=None)
        unlockParams: list[str] | None = Field(default=None)

    class LandmarkNodeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        nodeId: str
        landmarkId: str
        landmarkName: str
        landmarkPic: str | None
        landmarkSpecialPic: str
        landmarkDesList: list[str]

    class StoryNodeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        nodeId: str
        storyId: str
        storyKey: str
        storyName: str
        storyPic: str | None
        confirmDes: str
        storyDesList: list[str]

    class BattleNodeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        nodeId: str
        stageId: str

    class TreasureNodeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class EventNodeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        nodeId: str
        eventId: str
        endEventId: str

    class TechNodeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        nodeId: str
        techTreeId: str
        techTreeName: str
        techPic: str | None
        techSpecialPic: str
        endEventId: str
        confirmDes: str
        techDesList: list[str]
        missionIdList: list[str]

    class ChoiceNodeOptionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        canRepeat: bool
        eventId: str
        des: str
        unlockDes: str | None
        unlockCondType: str | None = Field(default=None)
        unlockParams: list[str] | None = Field(default=None)

    class ChoiceNodeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        nodeId: str
        choicePic: str | None
        isDisposable: bool
        choiceSpecialPic: str | None
        choiceName: str
        choiceDesList: list[str]
        cancelDes: str
        choiceNum: int
        optionList: list["Act17sideData.ChoiceNodeOptionData"]

    class EventData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        eventId: str
        eventPic: str | None
        eventSpecialPic: str | None
        eventTitle: str
        eventDesList: list[str]

    class ArchiveItemUnlockData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemId: str
        itemType: ActArchiveType
        unlockCondition: "Act17sideData.ArchiveItemUnlockCondition"
        nodeId: str | None
        stageParam: "Act17sideData.ArchiveItemStageUnlockParam"
        chapterId: str | None

    class TechTreeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        techTreeId: str
        sortId: int
        techTreeName: str
        defaultBranchId: str
        lockDes: str

    class TechTreeBranchData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        techTreeBranchId: str
        techTreeId: str
        techTreeBranchName: str
        techTreeBranchIcon: str
        techTreeBranchDesc: str
        runeData: RuneTable.PackedRuneData

    class MainlineChapterData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        chapterId: str
        chapterDes: str
        chapterIcon: "Act17sideData.ChapterIconType"
        unlockDes: str
        id: str

    class MainlineData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        mainlineId: str
        nodeId: str | None
        sortId: int
        missionSort: str
        zoneId: str
        mainlineDes: str
        focusNodeId: str | None

    class ZoneData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        zoneId: str
        unlockPlaceId: str | None
        unlockText: str

    class ConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        techTreeUnlockEventId: str
