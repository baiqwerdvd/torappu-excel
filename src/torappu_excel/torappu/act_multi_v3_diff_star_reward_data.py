from .act_multi_v3_map_diff_type import ActMultiV3MapDiffType
from .act_multi_v3_star_reward_data import ActMultiV3StarRewardData
from ..common import BaseStruct


class ActMultiV3DiffStarRewardData(BaseStruct):
    diffType: ActMultiV3MapDiffType
    starRewardDatas: list[ActMultiV3StarRewardData]
