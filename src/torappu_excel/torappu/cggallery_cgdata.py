from .cggallery_cgcomposite_data import CGGalleryCGCompositeData
from .cggallery_cgcomposite_type import CGGalleryCGCompositeType
from ..common import BaseStruct


class CGGalleryCGData(BaseStruct):
    cgId: str
    sortId: int
    compositeType: CGGalleryCGCompositeType
    compositeList: list[CGGalleryCGCompositeData] | None
    storySetId: str
