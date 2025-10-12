from pydantic import BaseModel, ConfigDict

from .recal_rune_const_data import RecalRuneConstData
from .recal_rune_season_data import RecalRuneSeasonData


class RecalRuneSharedData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    seasons: dict[str, RecalRuneSeasonData]
    constData: RecalRuneConstData
