from .sandbox_reward_item_config_data import SandboxRewardItemConfigData
from ..common import BaseStruct


class SandboxRewardData(BaseStruct):
    rewardList: list[SandboxRewardItemConfigData]
