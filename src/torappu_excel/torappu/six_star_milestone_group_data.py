from pydantic import BaseModel, ConfigDict

from .six_star_milestone_item_data import SixStarMilestoneItemData


class SixStarMilestoneGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    groupId: str
    stageIdList: list[str]
    milestoneDataList: list[SixStarMilestoneItemData]
