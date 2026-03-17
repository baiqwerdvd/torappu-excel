from .item_type import ItemType
from ..common import BaseStruct


class ArtGalleryCollectItemData(BaseStruct):
    itemId: str
    itemType: ItemType
    collectionSetId: str
    sortId: int
