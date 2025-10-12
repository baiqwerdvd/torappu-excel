from pydantic import BaseModel, ConfigDict, Field

from .sandbox_v2_craft_item_type import SandboxV2CraftItemType


class SandboxV2CraftItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
    isHidden: bool | None = Field(default=None)
