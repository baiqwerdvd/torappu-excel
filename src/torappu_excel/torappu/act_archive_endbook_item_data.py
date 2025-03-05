from ..common import BaseStruct

from msgspec import field


class ActArchiveEndbookItemData(BaseStruct):
    endBookId: str
    sortId: int
    endbookName: str
    unlockDesc: str
    textId: str
    enrollId: str | None = field(default=None)
    isLast: bool | None = field(default=None)
