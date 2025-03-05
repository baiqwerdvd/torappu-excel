from .item_bundle import ItemBundle
from ..common import BaseStruct

from msgspec import field


class RoguelikeTopicBPGrandPrize(BaseStruct):
    grandPrizeDisplayId: str
    sortId: int
    displayUnlockYear: int
    displayUnlockMonth: int
    acquireTitle: str
    purchaseTitle: str
    displayName: str
    displayDiscription: str
    bpLevelId: str
    itemBundle: ItemBundle | None = field(default=None)
    accordingCharId: str | None = field(default=None)
    accordingSkinId: str | None = field(default=None)
    detailAnnounceTime: str | None = field(default=None)
    picIdAftrerUnlock: str | None = field(default=None)
