from pydantic import BaseModel, ConfigDict


class ActMultiV3ConstToastData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    noRoom: str
    fullRoom: str
    roomIdFormatError: str
    roomIdCopySuccess: str
    banned: str
    serverOverload: str
    matchAliveFailed: str
    createRoomAliveFailed: str
    joinRoomAliveFailed: str
    roomOwnerReviseMap: str
    roomCollaboratorReviseMap: str
    roomCollaboratorJoinRoom: str
    roomCollaboratorExitRoom: str
    roomOwnerReviseMode: str
    roomCollaboratorReviseMode: str
    continuousClicks: str
    matchNoProject: str
    reportNoProject: str
    otherModeTrainingLock: str
    teamLock: str
    mentorLockTips: str
    unlockMentorInMatch: str
    unlockInverseMode: str
    unlockNewMapType: str
    teamFullLow: str
    teamFullHigh: str
    difficultUnlock: str
    weeklyAlbumTimeUnlock: str
    weeklyAlbumCommitUnlock: str
    squadLockHint: str
    squadEffectEditHint: str
    inverseModeUnlockHint: str
    noPhotoInTemplateHint: str
    cannotResubmitHint: str
    cannotSaveTitleChange: str
    matchPrepareRoomClose: str
    stageListViewTimeLockToast: str
