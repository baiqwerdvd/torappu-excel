from pydantic import BaseModel, ConfigDict

from .act_multi_v3_map_diff_type import ActMultiV3MapDiffType


class ActMultiV3InverseUnlockCond(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    diff: ActMultiV3MapDiffType
    requireStarCnt: int
