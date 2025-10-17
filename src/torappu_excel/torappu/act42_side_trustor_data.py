from ..common import BaseStruct


class Act42SideTrustorData(BaseStruct):
    trustorId: str
    sortId: int
    trustorName: str
    trustorIconSmall: str
    trustorIconLarge: str
    gunId: str
    taskList: list[str]
