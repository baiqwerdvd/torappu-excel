from .item_bundle import ItemBundle
from ..common import BaseStruct


class ArtGalleryCollectSetMissionData(BaseStruct):
    missionId: str
    requireItemCount: int
    rewardList: list[ItemBundle]
