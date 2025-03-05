from ..common import BaseStruct


class ActArchiveCapsuleItemData(BaseStruct):
    capsuleId: str
    capsuleSortId: int
    englishName: str
    enrollId: str | None
