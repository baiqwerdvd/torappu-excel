from .art_gallery_collect_item_data import ArtGalleryCollectItemData
from .art_gallery_collect_set_mission_data import ArtGalleryCollectSetMissionData
from .collect_type import CollectType
from ..common import BaseStruct


class ArtGalleryCollectSetData(BaseStruct):
    setId: str
    setName: str
    setType: CollectType
    sortId: int
    startTime: int
    completeTime: int
    items: list[ArtGalleryCollectItemData]
    displayMaxCount: int
    missionList: dict[str, ArtGalleryCollectSetMissionData]
