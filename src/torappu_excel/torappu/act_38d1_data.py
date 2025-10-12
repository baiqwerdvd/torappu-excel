from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class Act38D1Data(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class Act38D1NodeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        slotId: str
        groupId: str | None
        isUpper: bool
        adjacentSlotList: list[str]

    class Act38D1RoadData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        roadId: str
        startSlotId: str
        endSlotId: str

    class Act38D1RewardBoxData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        rewardBoxId: str
        roadId: str

    class Act38D1ExclusionGroupData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        groupId: str
        slotIdList: list[str]

    class Act38D1DimensionItemData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        desc: str
        maxScore: int

    class Act38D1CommentData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        sortId: int
        desc: str

    class Act38D1StageDetailData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        nodeDataMap: dict[str, "Act38D1Data.Act38D1NodeData"]
        roadDataMap: dict[str, "Act38D1Data.Act38D1RoadData"]
        rewardBoxDataMap: dict[str, "Act38D1Data.Act38D1RewardBoxData"]
        exclusionGroupDataMap: dict[str, "Act38D1Data.Act38D1ExclusionGroupData"]
        dimensionItemList: list["Act38D1Data.Act38D1DimensionItemData"]
        commentDataMap: dict[str, "Act38D1Data.Act38D1CommentData"]

    class Act38D1ConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
