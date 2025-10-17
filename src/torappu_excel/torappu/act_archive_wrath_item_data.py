from ..common import BaseStruct


class ActArchiveWrathItemData(BaseStruct):
    wrathId: str
    sortId: int
    picTitleId: str
    picSmallInactiveId: str | None
    picSmallActiveId: str
    picBigActiveId: str
    picBigInactiveId: str | None
    enrollId: str | None
    isSp: bool
