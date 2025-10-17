from .act_multi_v3_map_diff_type import ActMultiV3MapDiffType
from ..common import BaseStruct


class ActMultiV3InverseUnlockCond(BaseStruct):
    diff: ActMultiV3MapDiffType
    requireStarCnt: int
