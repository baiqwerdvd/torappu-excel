from ..common import BaseStruct


class FifthAnnivExploreConst(BaseStruct):
    prevRecordNum: int
    maxBoard: int
    valueMin: int
    valueMax: int
    targetStuckDesc: str
    stageStuckDesc: str
    missionName: str
    missionDesc: str
    choiceValueOrder: list[str]
    teamPassTargeDesc: str
    teamPassEndDesc: str
