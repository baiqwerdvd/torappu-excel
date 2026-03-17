from .item_bundle import ItemBundle
from ..common import BaseStruct


class MagazineLeafConst(BaseStruct):
    sysUnlockRewards: list[ItemBundle]
    leafDisplayMaxNum: int
    skinDefaultGainTime: int
    defaultLeafId: str
