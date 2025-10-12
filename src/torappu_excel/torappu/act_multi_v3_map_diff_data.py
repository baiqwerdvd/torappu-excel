from pydantic import BaseModel, ConfigDict

from .act_multi_v3_map_diff_type import ActMultiV3MapDiffType


class ActMultiV3MapDiffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    diffType: ActMultiV3MapDiffType
    name: str
