from pydantic import BaseModel, ConfigDict

from .act_multi_v3_match_pos_type import ActMultiV3MatchPosType
from .act_multi_v3_match_pos_unlock_cond import ActMultiV3MatchPosUnlockCond


class ActMultiV3MatchPosData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    matchPos: ActMultiV3MatchPosType
    sortId: int
    name: str
    desc: str | None
    posToast: str
    matchDesc: str
    unlockCond: ActMultiV3MatchPosUnlockCond | None
