from pydantic import BaseModel, ConfigDict

from .sandbox_item_type import SandboxItemType
from .sandbox_node_type import SandboxNodeType


class SandboxItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    itemType: SandboxItemType
    itemName: str
    itemUsage: str
    itemDesc: str
    itemRarity: int
    sortId: int
    recommendTypeList: list[SandboxNodeType] | None
    recommendPriority: int
    obtainApproach: str
