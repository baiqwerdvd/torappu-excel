from pydantic import BaseModel, ConfigDict, Field

from .building_data import BuildingData
from .item_bundle import ItemBundle


class PlayerBuildingTradingOrder(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    instId: int
    type: "BuildingData.OrderType"
    delivery: list[ItemBundle]
    gain: ItemBundle
    buff: "list[PlayerBuildingTradingOrder.TradingOrderBuff]"
    isViolated: bool | None = None
    specGoldTag: "PlayerBuildingTradingOrder.TradingGoldTag | None" = None

    class TradingOrderBuff(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        from_: str = Field(alias="from")
        param: int

    class TradingGoldTag(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        activated: bool
        from_: str = Field(alias="from")
