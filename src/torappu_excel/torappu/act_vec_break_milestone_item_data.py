from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActVecBreakMilestoneItemData(BaseStruct):
    milestoneId: str
    orderId: int
    tokenNum: int
    reward: ItemBundle
    availTime: int
