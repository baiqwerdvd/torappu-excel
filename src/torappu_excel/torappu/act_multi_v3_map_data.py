from ..common import BaseStruct


class ActMultiV3MapData(BaseStruct):
    stageId: str
    modeId: str
    sortId: int
    missionIdList: list[str]
    displayEnemyIdList: list[str]
    previewIconId: str
