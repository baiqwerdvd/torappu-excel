from .act_4fun_perform_word_data import Act4funPerformWordData
from ..common import BaseStruct


class Act4funPerformInfo(BaseStruct):
    performId: str
    performFinishedPicId: str | None
    fixedCmpGroup: str | None
    cmpGroups: list[str | None]
    words: list[Act4funPerformWordData]
