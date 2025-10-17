from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActMultiV3StarRewardData(BaseStruct):
    starNum: int
    rewards: list[ItemBundle]
    dailyMissionPoint: int
