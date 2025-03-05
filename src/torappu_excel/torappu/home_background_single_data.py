from ..common import BaseStruct


class HomeBackgroundSingleData(BaseStruct):
    bgId: str
    bgSortId: int
    bgStartTime: int
    bgName: str
    bgMusicId: str
    bgDes: str
    bgUsage: str
    obtainApproach: str
    unlockDesList: list[str]
    bgType: str = ""
