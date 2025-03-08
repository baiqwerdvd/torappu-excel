from .act_multi_v3_map_diff_type import ActMultiV3MapDiffType
from ..common import BaseStruct


class ActMultiV3MatchPosUnlockCond(BaseStruct):
    diff: ActMultiV3MapDiffType
    completeMapCount: int
    requireMapStar: int
    unlockHint: str
