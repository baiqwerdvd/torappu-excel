from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .rune_table import RuneTable


class Act42D0Data(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class Act42D0AreaDifficulty(StrEnum):
        NONE = "NONE"
        NORMAL = "NORMAL"
        HARD = "HARD"

    areaInfoData: dict[str, "Act42D0Data.Act42D0AreaInfoData"]
    stageInfoData: dict[str, "Act42D0Data.Act42D0StageInfoData"]
    effectGroupInfoData: dict[str, "Act42D0Data.Act42D0EffectGroupInfoData"]
    effectInfoData: dict[str, "Act42D0Data.Act42D0EffectInfoData"]
    challengeInfoData: dict[str, "Act42D0Data.Act42D0ChallengeInfoData"]
    stageRatingInfoData: dict[str, "Act42D0Data.Act42D0StageRatingInfoData"]
    milestoneData: list["Act42D0Data.Act42D0MilestoneData"]
    constData: "Act42D0Data.Act42D0ConstData"
    trackPointPeriodData: list[int]

    class Act42D0AreaInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        areaId: str
        sortId: int
        areaCode: str
        areaName: str
        difficulty: "Act42D0Data.Act42D0AreaDifficulty"
        areaDesc: str
        costLimit: int
        bossIcon: str
        bossId: str | None
        nextAreaStage: str | None

    class Act42D0StageInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        areaId: str
        stageCode: str
        sortId: int
        stageDesc: list[str]
        levelId: str
        code: str
        name: str
        loadingPicId: str

    class Act42D0EffectGroupInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        effectGroupId: str
        sortId: int
        effectGroupName: str

    class Act42D0EffectInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        effectId: str
        effectGroupId: str
        row: int
        col: int
        effectName: str
        effectIcon: str
        cost: int
        effectDesc: str
        unlockTime: int
        runeData: "RuneTable.PackedRuneData"

    class Act42D0ChallengeMissionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        missionId: str
        sortId: int
        stageId: str
        missionDesc: str
        milestoneCount: int

    class Act42D0ChallengeInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        stageDesc: str
        startTs: int
        endTs: int
        levelId: str
        code: str
        name: str
        loadingPicId: str
        challengeMissionData: list["Act42D0Data.Act42D0ChallengeMissionData"]

    class Act42D0StageRatingInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        areaId: str
        milestoneData: list["Act42D0Data.Act42D0RatingInfoData"]

    class Act42D0RatingInfoData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        ratingLevel: int
        costUpLimit: int
        achivement: str
        icon: str
        milestoneCount: int

    class Act42D0MilestoneData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        milestoneId: str
        orderId: int
        tokenNum: int
        item: ItemBundle

    class Act42D0ConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        milestoneId: str
        strifeName: str
        strifeDesc: str
        unlockDesc: str
        rewardDesc: str
        traumaDesc: str
        milestoneAreaName: str
        traumaName: str
