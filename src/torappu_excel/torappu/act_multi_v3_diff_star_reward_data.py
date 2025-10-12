from pydantic import BaseModel, ConfigDict

from .act_multi_v3_map_diff_type import ActMultiV3MapDiffType
from .act_multi_v3_star_reward_data import ActMultiV3StarRewardData


class ActMultiV3DiffStarRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    diffType: ActMultiV3MapDiffType
    starRewardDatas: list[ActMultiV3StarRewardData]
