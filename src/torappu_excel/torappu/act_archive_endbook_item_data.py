from msgspec import field

from ..common import BaseStruct


class ActArchiveEndbookItemData(BaseStruct):
    endBookId: str
    sortId: int
    endbookName: str
    unlockDesc: str
    textId: str
    enrollId: str | None = field(default=None)
    isLast: bool | None = field(default=None)
