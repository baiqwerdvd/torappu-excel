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
    templateId: str | None
    templateStartTime: int
    templateColor: str | None
    templateColor2: str | None
    skinDefaultPos: Vector2
    skinDefaultScale: float
    leafDecorMaxNumMap: dict[str, int]
