from pydantic import BaseModel, ConfigDict

from .sandbox_item_type import SandboxItemType


class SandboxRewardCommonConfig(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rewardItemId: str
    rewardItemType: SandboxItemType
    count: int
