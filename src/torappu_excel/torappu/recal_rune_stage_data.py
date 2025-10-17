from .recal_rune_rune_data import RecalRuneRuneData
from ..common import BaseStruct


class RecalRuneStageData(BaseStruct):
    stageId: str
    levelId: str
    juniorMedalId: str
    seniorMedalId: str
    juniorMedalScore: int
    seniorMedalScore: int
    runes: dict[str, RecalRuneRuneData]
    sourceName: str
    sourceType: str
    useName: bool
    levelName: str
    levelCode: str
    levelDesc: str
    fixedRuneSeriesName: str
    logoId: str
    mainPicId: str
    loadingPicId: str
