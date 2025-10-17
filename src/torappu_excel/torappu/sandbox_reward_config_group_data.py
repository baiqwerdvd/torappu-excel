from .sandbox_reward_common_config import SandboxRewardCommonConfig
from .sandbox_reward_data import SandboxRewardData
from .sandbox_trap_reward_config_data import SandboxTrapRewardConfigData
from ..common import BaseStruct


class SandboxRewardConfigGroupData(BaseStruct):
    stagePreviewRewardDict: dict[str, SandboxRewardData]
    stageDefaultPreviewRewardDict: dict[str, SandboxRewardData]
    rushPreviewRewardDict: dict[str, SandboxRewardData]
    stageRewardDict: dict[str, SandboxRewardData]
    rushRewardDict: dict[str, SandboxRewardData]
    trapRewardDict: dict[str, SandboxTrapRewardConfigData]
    enemyRewardDict: dict[str, SandboxRewardCommonConfig]
    keyWordData: dict[str, str]
