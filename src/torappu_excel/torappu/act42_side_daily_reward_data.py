from .item_bundle import ItemBundle
from ..common import BaseStruct


class Act42SideDailyRewardData(BaseStruct):
    completedCnt: int
    reward: ItemBundle
