from .sandbox_craft_item_type import SandboxCraftItemType
from ..common import BaseStruct


class SandboxCraftItemData(BaseStruct):
    itemId: str
    sortId: int
    getFrom: str
    npcId: str | None
    notObtainedDesc: str
    itemType: SandboxCraftItemType
