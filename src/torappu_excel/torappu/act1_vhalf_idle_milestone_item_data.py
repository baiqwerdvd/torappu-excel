from .item_bundle import ItemBundle
from ..common import BaseStruct


class Act1VHalfIdleMilestoneItemData(BaseStruct):
    milestoneId: str
    orderId: int
    tokenNum: int
    reward: ItemBundle
    availTime: int
