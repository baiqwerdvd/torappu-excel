from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActMultiV3WeeklyPhotoRewardData(BaseStruct):
    order: int
    titleDesc: str
    unlockTime: int
    rewards: list[ItemBundle]
