from pydantic import BaseModel, ConfigDict

from .sandbox_craft_item_type import SandboxCraftItemType


class SandboxCraftItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    sortId: int
    getFrom: str
    npcId: str | None
    notObtainedDesc: str
    itemType: SandboxCraftItemType
