from .act_multi_v3_match_pos_type import ActMultiV3MatchPosType
from .act_multi_v3_match_pos_unlock_cond import ActMultiV3MatchPosUnlockCond
from ..common import BaseStruct


class ActMultiV3MatchPosData(BaseStruct):
    matchPos: ActMultiV3MatchPosType
    sortId: int
    name: str
    desc: str
    posToast: str
    matchDesc: str
    unlockCond: ActMultiV3MatchPosUnlockCond
