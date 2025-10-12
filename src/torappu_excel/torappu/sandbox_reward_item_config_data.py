from pydantic import BaseModel, ConfigDict

from .sandbox_item_type import SandboxItemType


class SandboxRewardItemConfigData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rewardItem: str
    rewardType: SandboxItemType
