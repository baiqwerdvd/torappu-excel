from .act_17side_data import Act17sideData
from ..common import BaseStruct


class ActArchiveChapterLogData(BaseStruct):
    chapterName: str
    displayId: str
    unlockDes: str
    logs: list[str]
    chapterIcon: Act17sideData.ChapterIconType
