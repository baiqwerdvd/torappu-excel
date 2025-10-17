from msgspec import field

from .building_data import BuildingData
from .item_bundle import ItemBundle
from ..common import BaseStruct


class PlayerBuildingTradingOrder(BaseStruct):
    instId: int
    type: "BuildingData.OrderType"
    delivery: list[ItemBundle]
    gain: ItemBundle
    buff: "list[PlayerBuildingTradingOrder.TradingOrderBuff]"
    isViolated: bool | None = None
    specGoldTag: "PlayerBuildingTradingOrder.TradingGoldTag | None" = None

    class TradingOrderBuff(BaseStruct):
        from_: str = field(name="from")
        param: int

    class TradingGoldTag(BaseStruct):
        activated: bool
        from_: str = field(name="from")
