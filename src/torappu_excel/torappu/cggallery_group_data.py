from ..common import BaseStruct


class CGGalleryGroupData(BaseStruct):
    storySetId: str
    storylineId: str
    locationId: str
    displays: list[str]
