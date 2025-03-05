from .item_bundle import ItemBundle
from ..common import BaseStruct


class CrisisClientData(BaseStruct):
    seasonId: str
    startTs: int
    endTs: int
    name: str
    crisisRuneCoinUnlockItem: ItemBundle
    permBgm: str
    medalGroupId: str | None
    bgmHardPoint: int
    permBgmHard: str | None
