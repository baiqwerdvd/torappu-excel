from .art_gallery_collect_const_data import ArtGalleryCollectConstData
from .art_gallery_collect_set_data import ArtGalleryCollectSetData
from .art_gallery_collect_type_data import ArtGalleryCollectTypeData
from ..common import BaseStruct


class ArtGalleryCollectData(BaseStruct):
    collectionSets: dict[str, ArtGalleryCollectSetData]
    collectionTypes: dict[str, ArtGalleryCollectTypeData]
    constData: ArtGalleryCollectConstData
