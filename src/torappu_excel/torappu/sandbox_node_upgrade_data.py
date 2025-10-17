from .sandbox_building_item_type import SandboxBuildingItemType
from .sandbox_item_type import SandboxItemType
from ..common import BaseStruct


class SandboxNodeUpgradeData(BaseStruct):
    nodeUpdradeId: str
    name: str
    description: str
    upgradeDesc: str
    itemType: SandboxItemType
    itemSubType: SandboxBuildingItemType
    itemCnt: int
    itemRarity: int
