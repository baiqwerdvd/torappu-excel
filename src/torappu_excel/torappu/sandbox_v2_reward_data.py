from pydantic import BaseModel, ConfigDict

from .sandbox_v2_reward_item_config_data import SandboxV2RewardItemConfigData


class SandboxV2RewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rewardList: list[SandboxV2RewardItemConfigData]
