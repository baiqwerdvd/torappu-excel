from pydantic import BaseModel, ConfigDict

from .sandbox_building_item_type import SandboxBuildingItemType


class SandboxBuildingItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    itemSubType: SandboxBuildingItemType
    itemRarity: int
