from pydantic import BaseModel, ConfigDict


class ActivityEnemyDuelConstToastData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    createRoomAliveFailed: str
    joinRoomAliveFailed: str
    roomIdFormatError: str | None
    emptyRoomId: str
    noRoom: str
    continuousClicks: str
    matchAliveFailed: str
    serverOverloaded: str
    matchTimeout: str
    unlockMultiMode: str
    unlockRoomMode: str
    addFriendInRoom: str
    roomIdCopySuccess: str
    entryModeLock: str
