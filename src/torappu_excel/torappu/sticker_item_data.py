from .item_rarity import ItemRarity
from .sticker_type import StickerType
from ..common import BaseStruct


class StickerItemData(BaseStruct):
    id: str
    name: str
    stickerType: StickerType
    sortId: int
    desc: str
    usage: str
    approach: str
    rarity: ItemRarity
