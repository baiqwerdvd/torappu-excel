from pydantic import BaseModel, ConfigDict, Field

from .climb_tower_drop_display_info import ClimbTowerDropDisplayInfo
from .stage_data import StageData
from .weight_item_bundle import WeightItemBundle


class ClimbTowerLevelDropInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    displayRewards: list["StageData.DisplayRewards"] | None
    displayDetailRewards: list["StageData.DisplayDetailRewards"] | None
    passRewards: list[list[WeightItemBundle]] | None = Field(default=None)
    displayDropInfo: dict[str, ClimbTowerDropDisplayInfo] | None = Field(default=None)
