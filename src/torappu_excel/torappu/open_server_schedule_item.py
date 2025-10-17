from ..common import BaseStruct


class OpenServerScheduleItem(BaseStruct):
    id: str
    versionId: str
    startTs: int
    endTs: int
    totalCheckinDescption: str
    chainLoginDescription: str
    charImg: str
