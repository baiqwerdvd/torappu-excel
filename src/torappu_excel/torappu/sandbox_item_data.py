from .sandbox_item_type import SandboxItemType
from .sandbox_node_type import SandboxNodeType
from ..common import BaseStruct


class SandboxItemData(BaseStruct):
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
