from .item_bundle import ItemBundle
from ..common import BaseStruct


class RetroTrailRewardItem(BaseStruct):
    trailRewardId: str
    starCount: int
    rewardItem: ItemBundle
