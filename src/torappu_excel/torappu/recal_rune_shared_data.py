from .recal_rune_const_data import RecalRuneConstData
from .recal_rune_season_data import RecalRuneSeasonData
from ..common import BaseStruct


class RecalRuneSharedData(BaseStruct):
    seasons: dict[str, RecalRuneSeasonData]
    constData: RecalRuneConstData
