from .shop_cond_trig_package_type import ShopCondTrigPackageType
from ..common import BaseStruct


class ShopClientGPData(BaseStruct):
    goodId: str
    giftPackageId: str
    displayName: str
    condTrigPackageType: ShopCondTrigPackageType
