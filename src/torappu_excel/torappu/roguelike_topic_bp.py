from .item_type import ItemType
from ..common import BaseStruct

from msgspec import field


class RoguelikeTopicBP(BaseStruct):
    id_: str = field(name="id")
    level: int
    tokenNum: int
    nextTokenNum: int
    itemID: str
    itemType: ItemType
    itemCount: int
    isGoodPrize: bool
    isGrandPrize: bool
