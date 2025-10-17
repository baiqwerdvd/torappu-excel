from enum import StrEnum

from .shared_models import ActivityTable
from ..common import BaseStruct


class ActivityMultiplayData(BaseStruct):
    class StageDifficulty(StrEnum):
        NONE = "NONE"
        EASY = "EASY"
        NORMAL = "NORMAL"
        HARD = "HARD"

    stages: dict[str, "ActivityMultiplayData.StageData"]
    stageGroups: dict[str, "ActivityMultiplayData.StageGroupData"]
    missionExtras: dict[str, "ActivityMultiplayData.MissionExtraData"]
    roomMessages: list["ActivityMultiplayData.RoomMessageData"]
    constData: "ActivityMultiplayData.ConstData"
    unlockConds: list[ActivityTable.CustomUnlockCond]

    class StageData(BaseStruct):
        stageId: str
        levelId: str
        groupId: str
        difficulty: "ActivityMultiplayData.StageDifficulty"
        loadingPicId: str
        dangerLevel: str
        unlockConds: list[str]

    class StageGroupData(BaseStruct):
        groupId: str
        sortId: int
        code: str
        name: str
        description: str

    class MissionExtraData(BaseStruct):
        missionId: str
        isHard: bool

    class RoomMessageData(BaseStruct):
        sortId: int
        picId: str

    class ConstData(BaseStruct):
        linkActId: str
        maxRetryTimeInTeamRoom: int
        maxRetryTimeInMatchRoom: int
        maxRetryTimeInBattle: int
        maxOperatorDelay: float
        maxPlaySpeed: float
        delayTimeNeedTip: float
        blockTimeNeedTip: float
        hideTeamNameFlag: bool
        settleRetryTime: float
