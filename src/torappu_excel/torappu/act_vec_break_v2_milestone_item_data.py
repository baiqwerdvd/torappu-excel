from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActVecBreakV2MilestoneItemData(BaseStruct):
    milestoneId: str
    orderId: int
    tokenNum: int
    reward: ItemBundle
    availTime: int
