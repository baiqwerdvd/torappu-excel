from .crisis_v2_appraise_wrap import CrisisV2AppraiseWrap
from .crisis_v2_const_data import CrisisV2ConstData
from .crisis_v2_season_info import CrisisV2SeasonInfo
from .rune_data import RuneData
from ..common import BaseStruct


class CrisisV2SharedData(BaseStruct):
    seasonInfoDataMap: dict[str, CrisisV2SeasonInfo]
    scoreLevelToAppraiseDataMap: dict[str, CrisisV2AppraiseWrap]
    constData: CrisisV2ConstData
    battleCommentRuneData: dict[str, list[RuneData]]
