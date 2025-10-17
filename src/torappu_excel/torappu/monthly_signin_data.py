from .item_type import ItemType
from ..common import BaseStruct


class MonthlySignInData(BaseStruct):
    itemId: str
    itemType: ItemType
    count: int
