from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .shared_models import ActivityTable


class ActivityMultiplayData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class StageData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        levelId: str
        groupId: str
        difficulty: "ActivityMultiplayData.StageDifficulty"
        loadingPicId: str
        dangerLevel: str
        unlockConds: list[str]

    class StageGroupData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        groupId: str
        sortId: int
        code: str
        name: str
        description: str

    class MissionExtraData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        missionId: str
        isHard: bool

    class RoomMessageData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        sortId: int
        picId: str

    class ConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
