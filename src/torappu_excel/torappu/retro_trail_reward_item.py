from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class RetroTrailRewardItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    trailRewardId: str
    starCount: int
    rewardItem: ItemBundle
