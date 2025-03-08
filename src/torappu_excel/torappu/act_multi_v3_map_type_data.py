from .act_multi_v3_map_diff_type import ActMultiV3MapDiffType
from .act_multi_v3_map_mode_type import ActMultiV3MapModeType
from ..common import BaseStruct


class ActMultiV3MapTypeData(BaseStruct):
    modeId: str
    mode: ActMultiV3MapModeType
    difficulty: ActMultiV3MapDiffType
    isDefaultSelectInQuickMatch: bool
    squadMax: int
    matchUnlockModeId: str
    matchUnlockParam: int
    stageIdInModeList: list[str]
    unlockHint: str
