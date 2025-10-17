from .act1_vhalf_idle_item_type import Act1VHalfIdleItemType
from ..common import BaseStruct


class Act1VHalfIdleItemData(BaseStruct):
    actId: str
    itemId: str
    itemType: Act1VHalfIdleItemType
    itemName: str
    sortId: int
    iconId: str
    funcDesc: str
    flavorDesc: str
    obtainApproach: str
    showInInventory: bool
