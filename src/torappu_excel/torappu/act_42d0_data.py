from enum import StrEnum

from .item_bundle import ItemBundle
from .rune_table import RuneTable
from ..common import BaseStruct


class Act42D0Data(BaseStruct):
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

    class Act42D0AreaInfoData(BaseStruct):
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

    class Act42D0StageInfoData(BaseStruct):
        stageId: str
        areaId: str
        stageCode: str
        sortId: int
        stageDesc: list[str]
        levelId: str
        code: str
        name: str
        loadingPicId: str

    class Act42D0EffectGroupInfoData(BaseStruct):
        effectGroupId: str
        sortId: int
        effectGroupName: str

    class Act42D0EffectInfoData(BaseStruct):
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

    class Act42D0ChallengeMissionData(BaseStruct):
        missionId: str
        sortId: int
        stageId: str
        missionDesc: str
        milestoneCount: int

    class Act42D0ChallengeInfoData(BaseStruct):
        stageId: str
        stageDesc: str
        startTs: int
        endTs: int
        levelId: str
        code: str
        name: str
        loadingPicId: str
        challengeMissionData: list["Act42D0Data.Act42D0ChallengeMissionData"]

    class Act42D0StageRatingInfoData(BaseStruct):
        stageId: str
        areaId: str
        milestoneData: list["Act42D0Data.Act42D0RatingInfoData"]

    class Act42D0RatingInfoData(BaseStruct):
        ratingLevel: int
        costUpLimit: int
        achivement: str
        icon: str
        milestoneCount: int

    class Act42D0MilestoneData(BaseStruct):
        milestoneId: str
        orderId: int
        tokenNum: int
        item: ItemBundle

    class Act42D0ConstData(BaseStruct):
        milestoneId: str
        strifeName: str
        strifeDesc: str
        unlockDesc: str
        rewardDesc: str
        traumaDesc: str
        milestoneAreaName: str
        traumaName: str
