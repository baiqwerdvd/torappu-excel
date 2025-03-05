from .sandbox_v2_craft_item_type import SandboxV2CraftItemType
from ..common import BaseStruct

from msgspec import field


class SandboxV2CraftItemData(BaseStruct):
    itemId: str
    type_: SandboxV2CraftItemType | None = field(name="type")
    buildingUnlockDesc: str
    materialItems: dict[str, int]
    upgradeItems: dict[str, int] | None
    outputRatio: int
    withdrawRatio: int
    repairCost: int
    craftGroupId: str
    recipeLevel: int
    isHidden: bool | None = field(default=None)
