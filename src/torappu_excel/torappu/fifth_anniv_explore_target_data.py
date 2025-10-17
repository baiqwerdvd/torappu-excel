from ..common import BaseStruct


class FifthAnnivExploreTargetData(BaseStruct):
    id: str
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
