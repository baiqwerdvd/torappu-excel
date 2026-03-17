from .collect_type import CollectType
from ..common import BaseStruct


class ArtGalleryCollectTypeData(BaseStruct):
    setType: CollectType
    typeName: str
    typeEngNameFilterPic: str
    typeEngNamePic: str
    typeFilterSelectIcon: str
    typeFilterUnselectIcon: str
    setIdList: list[str]
    sortId: int
