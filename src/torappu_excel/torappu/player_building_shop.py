from pydantic import BaseModel, ConfigDict

from .player_building_shop_output_item import PlayerBuildingShopOutputItem
from .player_building_shop_stock import PlayerBuildingShopStock


class PlayerBuildingShop(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stock: list[PlayerBuildingShopStock]
    outputItem: list[PlayerBuildingShopOutputItem]
