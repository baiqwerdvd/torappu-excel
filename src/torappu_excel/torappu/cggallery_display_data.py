from .cggallery_cgsource import CGGalleryCGSource
from ..common import BaseStruct


class CGGalleryDisplayData(BaseStruct):
    displayId: str
    cgList: list[str]
    cgSource: CGGalleryCGSource
    displayName: str
    displayDesc: str
    storySetId: str
    sortId: int
    relatedStoryId: str | None
    relatedStageId: str | None
