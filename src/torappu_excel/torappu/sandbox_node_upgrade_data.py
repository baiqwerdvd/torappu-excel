from pydantic import BaseModel, ConfigDict

from .sandbox_building_item_type import SandboxBuildingItemType
from .sandbox_item_type import SandboxItemType


class SandboxNodeUpgradeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeUpdradeId: str
    name: str
    description: str
    upgradeDesc: str
    itemType: SandboxItemType
    itemSubType: SandboxBuildingItemType
    itemCnt: int
    itemRarity: int
