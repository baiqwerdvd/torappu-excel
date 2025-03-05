from ..common import BaseStruct


class ActArchiveFragmentItemData(BaseStruct):
    fragmentId: str
    sortId: int
    enrollConditionId: str | None
