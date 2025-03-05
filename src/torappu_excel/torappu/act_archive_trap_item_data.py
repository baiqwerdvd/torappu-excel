from ..common import BaseStruct


class ActArchiveTrapItemData(BaseStruct):
    trapId: str
    trapSortId: int
    orderId: str
    enrollId: str | None
