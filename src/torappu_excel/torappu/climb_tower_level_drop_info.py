from .climb_tower_drop_display_info import ClimbTowerDropDisplayInfo
from .stage_data import StageData
from .weight_item_bundle import WeightItemBundle
from ..common import BaseStruct

from msgspec import field


class ClimbTowerLevelDropInfo(BaseStruct):
    displayRewards: list["StageData.DisplayRewards"] | None
    displayDetailRewards: list["StageData.DisplayDetailRewards"] | None
    passRewards: list[list[WeightItemBundle]] | None = field(default=None)
    displayDropInfo: dict[str, ClimbTowerDropDisplayInfo] | None = field(default=None)
