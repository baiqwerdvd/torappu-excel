from ..common import BaseStruct


class ActivityEnemyDuelConstToastData(BaseStruct):
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
