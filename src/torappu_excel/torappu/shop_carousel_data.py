from pydantic import BaseModel, ConfigDict

from .shop_route_target import ShopRouteTarget


class ShopCarouselData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    items: list["ShopCarouselData.Item"]

    class Item(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        spriteId: str
        startTime: int
        endTime: int
        cmd: ShopRouteTarget
        param1: str | None
        skinId: str
        furniId: str | None
