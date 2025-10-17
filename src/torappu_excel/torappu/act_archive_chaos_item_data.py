from ..common import BaseStruct


class ActArchiveChaosItemData(BaseStruct):
    id: str
    isHidden: bool
    enrollId: str | None
    sortId: int
