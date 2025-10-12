from pydantic import BaseModel, ConfigDict

from .shop_route_target import ShopRouteTarget


class ShopRecommendData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    imgId: str
    slotIndex: int
    cmd: ShopRouteTarget
    param1: str | None
    param2: str | None
    skinId: str | None
