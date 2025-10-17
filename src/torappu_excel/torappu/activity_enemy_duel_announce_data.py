from ..common import BaseStruct


class ActivityEnemyDuelAnnounceData(BaseStruct):
    startTs: int
    endTs: int
    announceText: str
    showNew: bool
