from msgspec import field

from .sandbox_v2_craft_item_type import SandboxV2CraftItemType
from ..common import BaseStruct


class SandboxV2CraftItemData(BaseStruct):
    itemId: str
    type: SandboxV2CraftItemType | None
    buildingUnlockDesc: str
    materialItems: dict[str, int]
    upgradeItems: dict[str, int] | None
    outputRatio: int
    withdrawRatio: int
    repairCost: int
    craftGroupId: str
    recipeLevel: int
    isHidden: bool | None = field(default=None)
