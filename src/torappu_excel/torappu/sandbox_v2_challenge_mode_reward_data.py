from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class SandboxV2ChallengeModeRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rewardId: str
    sortId: int
    rewardDay: int
    rewardItemList: list[ItemBundle]
