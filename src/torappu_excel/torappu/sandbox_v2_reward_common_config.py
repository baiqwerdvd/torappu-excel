from pydantic import BaseModel, ConfigDict

from .sandbox_perm_item_type import SandboxPermItemType


class SandboxV2RewardCommonConfig(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rewardItemId: str
    rewardItemType: SandboxPermItemType
    count: int
