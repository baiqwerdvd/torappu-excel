from pydantic import BaseModel, ConfigDict

from .sandbox_v2_reward_common_config import SandboxV2RewardCommonConfig
from .sandbox_v2_reward_data import SandboxV2RewardData


class SandboxV2RewardConfigGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageMapPreviewRewardDict: dict[str, SandboxV2RewardData]
    stageDetailPreviewRewardDict: dict[str, SandboxV2RewardData]
    trapRewardDict: dict[str, SandboxV2RewardCommonConfig]
    enemyRewardDict: dict[str, SandboxV2RewardCommonConfig]
    unitPreviewRewardDict: dict[str, SandboxV2RewardData]
    stageRewardDict: dict[str, SandboxV2RewardData]
    rushPreviewRewardDict: dict[str, SandboxV2RewardData]
