from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActivityEnemyDuelMilestoneItemData(BaseStruct):
    milestoneId: str
    orderId: int
    tokenNum: int
    reward: ItemBundle
    availTime: int
