from .six_star_milestone_item_data import SixStarMilestoneItemData
from ..common import BaseStruct


class SixStarMilestoneGroupData(BaseStruct):
    groupId: str
    stageIdList: list[str]
    milestoneDataList: list[SixStarMilestoneItemData]
