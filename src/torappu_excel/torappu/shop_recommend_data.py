from .shop_route_target import ShopRouteTarget
from ..common import BaseStruct


class ShopRecommendData(BaseStruct):
    imgId: str
    slotIndex: int
    cmd: ShopRouteTarget
    param1: str | None
    param2: str | None
    skinId: str | None
