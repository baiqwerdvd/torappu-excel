from .act_ark_hub_item_type import ActArkHubItemType
from .item_rarity import ItemRarity
from ..common import BaseStruct


class ActArkHubItemData(BaseStruct):
    itemId: str
    itemNumId: int
    itemType: ActArkHubItemType
    itemName: str
    itemUsage: str
    itemDesc: str
    obtainApproach: str
    stackLimit: int
    maxEffectCount: int
    rarity: ItemRarity
    itemSortId: int
    isUsable: bool
    isShow: bool
    accumulateDesc: str | None
