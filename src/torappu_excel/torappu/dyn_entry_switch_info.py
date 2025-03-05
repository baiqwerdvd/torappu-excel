from ..common import BaseStruct


class DynEntrySwitchInfo(BaseStruct):
    entryId: str
    sortId: int
    stageId: str | None
