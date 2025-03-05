from ..common import BaseStruct

from msgspec import field


class FifthAnnivExploreTargetData(BaseStruct):
    id_: str = field(name="id")
    linkStageId: str
    targetValues: dict[str, int]
    lockedLevelId: str
    isEnd: bool
    name: str
    desc: str
    successDesc: str
    successIconId: str
    requireEventId: str | None
    endName: str | None
