from pydantic import BaseModel, ConfigDict

from .sandbox_reward_item_config_data import SandboxRewardItemConfigData


class SandboxRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rewardList: list[SandboxRewardItemConfigData]
