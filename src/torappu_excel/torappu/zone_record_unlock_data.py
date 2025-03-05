from ..common import BaseStruct


class ZoneRecordUnlockData(BaseStruct):
    noteId: str
    zoneId: str
    initialName: str
    finalName: str | None
    accordingExposeId: str | None
    initialDes: str
    finalDes: str | None
    remindDes: str | None
