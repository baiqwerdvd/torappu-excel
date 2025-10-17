from .sandbox_v2_reward_item_config_data import SandboxV2RewardItemConfigData
from ..common import BaseStruct


class SandboxV2RewardData(BaseStruct):
    rewardList: list[SandboxV2RewardItemConfigData]
