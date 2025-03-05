from ..common import BaseStruct

from msgspec import field


class FifthAnnivExploreStageData(BaseStruct):
    id_: str = field(name="id")
    eventCount: int
    prevNodeCount: int
    stageNum: int
    stageEventNum: int
    stageDisplayNum: str
    name: str | None
    desc: str | None
    nextStageId: str | None
    stageFailureDescription: str | None
