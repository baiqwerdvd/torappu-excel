from pydantic import BaseModel, ConfigDict

from .sandbox_perm_item_type import SandboxPermItemType


class SandboxPermItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    itemType: SandboxPermItemType
    itemName: str
    itemUsage: str
    itemDesc: str
    itemRarity: int
    sortId: int
    obtainApproach: str
