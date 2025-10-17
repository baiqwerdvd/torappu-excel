from ..common import BaseStruct


class ChapterData(BaseStruct):
    chapterId: str
    chapterName: str
    chapterName2: str
    chapterIndex: int
    preposedChapterId: str | None
    startZoneId: str
    endZoneId: str
    chapterEndStageId: str
