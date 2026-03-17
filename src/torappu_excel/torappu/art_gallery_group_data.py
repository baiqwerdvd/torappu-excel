from .art_gallery_item_data import ArtGalleryItemData
from ..common import BaseStruct


class ArtGalleryGroupData(BaseStruct):
    type: str
    title: str
    sortId: int
    items: list[ArtGalleryItemData]
