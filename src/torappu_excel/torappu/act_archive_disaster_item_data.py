from ..common import BaseStruct


class ActArchiveDisasterItemData(BaseStruct):
    disasterId: str
    sortId: int
    enrollConditionId: str | None
    picSmallId: str
    picBigActiveId: str
    picBigInactiveId: str
