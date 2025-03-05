from .shop_route_target import ShopRouteTarget
from ..common import BaseStruct


class ShopCarouselData(BaseStruct):
    items: list["ShopCarouselData.Item"]

    class Item(BaseStruct):
        spriteId: str
        startTime: int
        endTime: int
        cmd: ShopRouteTarget
        param1: str | None
        skinId: str
        furniId: str | None
