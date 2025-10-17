from .item_bundle import ItemBundle
from .six_star_milestone_reward_type import SixStarMilestoneRewardType
from ..common import BaseStruct


class SixStarMilestoneItemData(BaseStruct):
    id: str
    sortId: int
    nodePoint: int
    rewardType: SixStarMilestoneRewardType
    unlockStageFog: str | None
    unlockStageId: str | None
    unlockStageName: str | None
    rewardList: list[ItemBundle]
