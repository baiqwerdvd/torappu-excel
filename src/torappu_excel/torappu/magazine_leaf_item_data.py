from .item_rarity import ItemRarity
from .magazine_leaf_type import MagazineLeafType
from .vector2 import Vector2
from ..common import BaseStruct


class MagazineLeafItemData(BaseStruct):
    leafId: str
    leafType: MagazineLeafType
    sortId: int
    startTime: int
    name: str
    desc: str
    usage: str
    approach: str
    rarity: ItemRarity
    templateId: str
    templateStartTime: int
    templateColor: str
    skinDefaultPos: Vector2
    skinDefaultScale: float
    leafDecorMaxNumMap: dict[str, int]
