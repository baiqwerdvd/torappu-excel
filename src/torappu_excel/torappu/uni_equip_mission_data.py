from ..common import BaseStruct


class UniEquipMissionData(BaseStruct):
    template: str | None
    desc: str | None
    paramList: list[str]
    uniEquipMissionId: str
    uniEquipMissionSort: int
    uniEquipId: str
    jumpStageId: str | None


class UniEquipMissionDataOld(BaseStruct):
    template: str | None
    desc: str | None
    paramList: list[str]
    uniEquipMissionId: str
    uniEquipMissionSort: int
    uniEquipId: str
