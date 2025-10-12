from pydantic import BaseModel, ConfigDict

from .crisis_v2_appraise_wrap import CrisisV2AppraiseWrap
from .crisis_v2_const_data import CrisisV2ConstData
from .crisis_v2_season_info import CrisisV2SeasonInfo
from .recal_rune_shared_data import RecalRuneSharedData
from .rune_data import RuneData


class CrisisV2SharedData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    seasonInfoDataMap: dict[str, CrisisV2SeasonInfo]
    scoreLevelToAppraiseDataMap: dict[str, CrisisV2AppraiseWrap]
    constData: CrisisV2ConstData
    battleCommentRuneData: dict[str, list[RuneData]]
    recalRuneData: RecalRuneSharedData
