from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .six_star_milestone_reward_type import SixStarMilestoneRewardType


class SixStarMilestoneItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    sortId: int
    nodePoint: int
    rewardType: SixStarMilestoneRewardType
    unlockStageFog: str | None
    unlockStageId: str | None
    unlockStageName: str | None
    rewardList: list[ItemBundle]
