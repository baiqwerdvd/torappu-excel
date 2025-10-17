from .sandbox_v2_reward_common_config import SandboxV2RewardCommonConfig
from .sandbox_v2_reward_data import SandboxV2RewardData
from ..common import BaseStruct


class SandboxV2RewardConfigGroupData(BaseStruct):
    stageMapPreviewRewardDict: dict[str, SandboxV2RewardData]
    stageDetailPreviewRewardDict: dict[str, SandboxV2RewardData]
    trapRewardDict: dict[str, SandboxV2RewardCommonConfig]
    enemyRewardDict: dict[str, SandboxV2RewardCommonConfig]
    unitPreviewRewardDict: dict[str, SandboxV2RewardData]
    stageRewardDict: dict[str, SandboxV2RewardData]
    rushPreviewRewardDict: dict[str, SandboxV2RewardData]
