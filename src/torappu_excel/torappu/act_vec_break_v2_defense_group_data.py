from ..common import BaseStruct


class ActVecBreakV2DefenseGroupData(BaseStruct):
    groupId: str | None
    sortId: int
    orderedStageList: list[str]
