from ..common import BaseStruct


class SOCharMissionGroup(BaseStruct):
    groupId: str
    missionIds: list[str]
    startTs: int
    endTs: int
