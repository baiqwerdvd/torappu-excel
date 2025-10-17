from .item_bundle import ItemBundle
from ..common import BaseStruct


class Act6FunAchievementRewardData(BaseStruct):
    reward: ItemBundle
    sortId: int
    achievementCount: int
