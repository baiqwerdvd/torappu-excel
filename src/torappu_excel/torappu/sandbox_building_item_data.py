from .sandbox_building_item_type import SandboxBuildingItemType
from ..common import BaseStruct


class SandboxBuildingItemData(BaseStruct):
    itemId: str
    itemSubType: SandboxBuildingItemType
    itemRarity: int
