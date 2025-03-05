from ..common import BaseStruct

from msgspec import field


class OpenServerScheduleItem(BaseStruct):
    id_: str = field(name="id")
    versionId: str
    startTs: int
    endTs: int
    totalCheckinDescption: str
    chainLoginDescription: str
    charImg: str
