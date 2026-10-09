from ..common import BaseStruct


class ActArchiveScrapItemData(BaseStruct):
    scrapId: str
    sortId: int
    enrollConditionId: str | None
