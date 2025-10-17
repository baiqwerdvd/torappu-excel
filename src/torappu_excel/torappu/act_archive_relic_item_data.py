from ..common import BaseStruct


class ActArchiveRelicItemData(BaseStruct):
    relicId: str
    relicSortId: int
    relicGroupId: int
    orderId: str
    isSpRelic: bool
    enrollId: str | None
