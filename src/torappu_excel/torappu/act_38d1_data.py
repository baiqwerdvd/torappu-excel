from enum import StrEnum

from ..common import BaseStruct

from msgspec import field


class Act38D1Data(BaseStruct):
    class Act38D1NodeSlotType(StrEnum):
        NONE = "NONE"
        UNKNOW = "UNKNOW"
        NORMAL = "NORMAL"
        KEYPOINT = "KEYPOINT"
        TREASURE = "TREASURE"
        DAILY = "DAILY"
        START = "START"

    class Act38D1NodeSlotState(StrEnum):
        OPEN = "OPEN"
        TEMPCLOSE = "TEMPCLOSE"

    class Act38D1AppraiseType(StrEnum):
        RANK_D = "RANK_D"
        RANK_C = "RANK_C"
        RANK_B = "RANK_B"
        RANK_A = "RANK_A"
        RANK_S = "RANK_S"
        RANK_SS = "RANK_SS"
        RANK_SSS = "RANK_SSS"

    class Act38D1StageType(StrEnum):
        PERMANENT = "PERMANENT"
        TEMPORARY = "TEMPORARY"

    scoreLevelToAppraiseDataMap: dict[str, "Act38D1Data.Act38D1AppraiseType"]
    detailDataMap: dict[str, "Act38D1Data.Act38D1StageDetailData"]
    constData: "Act38D1Data.Act38D1ConstData"
    trackPointPeriodData: list[int]

    class Act38D1NodeData(BaseStruct):
        slotId: str
        groupId: str | None
        isUpper: bool
        adjacentSlotList: list[str]

    class Act38D1RoadData(BaseStruct):
        roadId: str
        startSlotId: str
        endSlotId: str

    class Act38D1RewardBoxData(BaseStruct):
        rewardBoxId: str
        roadId: str

    class Act38D1ExclusionGroupData(BaseStruct):
        groupId: str
        slotIdList: list[str]

    class Act38D1DimensionItemData(BaseStruct):
        desc: str
        maxScore: int

    class Act38D1CommentData(BaseStruct):
        id_: str = field(name="id")
        sortId: int
        desc: str

    class Act38D1StageDetailData(BaseStruct):
        nodeDataMap: dict[str, "Act38D1Data.Act38D1NodeData"]
        roadDataMap: dict[str, "Act38D1Data.Act38D1RoadData"]
        rewardBoxDataMap: dict[str, "Act38D1Data.Act38D1RewardBoxData"]
        exclusionGroupDataMap: dict[str, "Act38D1Data.Act38D1ExclusionGroupData"]
        dimensionItemList: list["Act38D1Data.Act38D1DimensionItemData"]
        commentDataMap: dict[str, "Act38D1Data.Act38D1CommentData"]

    class Act38D1ConstData(BaseStruct):
        redScoreThreshold: int
        detailBkgRedThreshold: int
        voiceGrade: int
        stageInfoTitle: str
        missionListReceiveRewardText: str
        missionListChangeMapText: str
        missionListCompleteTagText: str
        mapStartBattleText: str
        mapJumpDailyMapText: str
        mapRewardReceivedText: str
