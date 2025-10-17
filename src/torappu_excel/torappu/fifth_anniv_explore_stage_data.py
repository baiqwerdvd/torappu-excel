from ..common import BaseStruct


class FifthAnnivExploreStageData(BaseStruct):
    id: str
    eventCount: int
    prevNodeCount: int
    stageNum: int
    stageEventNum: int
    stageDisplayNum: str
    name: str | None
    desc: str | None
    nextStageId: str | None
    stageFailureDescription: str | None
