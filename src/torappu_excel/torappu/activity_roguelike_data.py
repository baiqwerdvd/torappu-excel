from .item_bundle import ItemBundle
from .item_type import ItemType
from .shared_models import ActivityTable
from ..common import BaseStruct


class ActivityRoguelikeData(BaseStruct):
    outBuffInfos: dict[str, "ActivityRoguelikeData.OuterBuffUnlockInfoData"]
    apSupplyOutOfDateDict: dict[str, int]
    outerBuffToken: str
    shopToken: str
    relicUnlockTime: int
    milestoneTokenRatio: float
    outerBuffTokenRatio: float
    relicTokenRatio: float
    relicOuterBuffTokenRatio: float
    reOpenCoolDown: int
    tokenItem: ItemBundle
    charStoneId: str
    milestone: list["ActivityRoguelikeData.MileStoneItemInfo"]
    unlockConds: list[ActivityTable.CustomUnlockCond]

    class OuterBuffUnlockInfo(BaseStruct):
        buffLevel: int
        name: str
        iconId: str
        description: str
        usage: str
        itemId: str
        itemType: ItemType
        cost: int

    class OuterBuffUnlockInfoData(BaseStruct):
        buffId: str
        buffUnlockInfos: dict[str, "ActivityRoguelikeData.OuterBuffUnlockInfo"]

    class MileStoneItemInfo(BaseStruct):
        mileStoneId: str
        orderId: int
        tokenNum: int
        item: ItemBundle
