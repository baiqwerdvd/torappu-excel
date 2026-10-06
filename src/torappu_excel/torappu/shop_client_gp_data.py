from msgspec import field

from .shop_cond_trig_package_type import ShopCondTrigPackageType
from ..common import BaseStruct


class ShopClientGPData(BaseStruct):
    goodId: str
    displayName: str
    condTrigPackageType: ShopCondTrigPackageType
    giftPackageId: str | None = field(default=None)
