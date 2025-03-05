from ..common import BaseStruct


class GuideMissionGroupInfo(BaseStruct):
    groupId: str
    sortId: int
    shortName: str
    unlockDesc: str | None
