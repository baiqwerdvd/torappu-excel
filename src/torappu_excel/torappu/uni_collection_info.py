from .item_bundle import ItemBundle
from ..common import BaseStruct


class UniCollectionInfo(BaseStruct):
    uniCollectionItemId: str
    uniqueItem: list[ItemBundle]
