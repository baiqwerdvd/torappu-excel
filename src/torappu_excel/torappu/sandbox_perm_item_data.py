from .sandbox_perm_item_type import SandboxPermItemType
from ..common import BaseStruct


class SandboxPermItemData(BaseStruct):
    itemId: str
    itemType: SandboxPermItemType
    itemName: str
    itemUsage: str
    itemDesc: str
    itemRarity: int
    sortId: int
    obtainApproach: str
