from .item_bundle import ItemBundle
from ..common import BaseStruct


class ActSandboxData(BaseStruct):
    milestoneDataList: list["ActSandboxData.MilestoneData"]
    milestoneTokenId: str

    class MilestoneData(BaseStruct):
        milestoneId: str
        orderId: int
        tokenId: str
        tokenNum: int
        item: ItemBundle
        isPrecious: bool
