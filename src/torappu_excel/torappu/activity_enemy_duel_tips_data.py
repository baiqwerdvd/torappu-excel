from ..common import BaseStruct


class ActivityEnemyDuelTipsData(BaseStruct):
    id: str
    txt: str
    weight: int
    modeIds: list[str] | None
