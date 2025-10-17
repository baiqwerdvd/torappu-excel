from .player_building_shop_output_item import PlayerBuildingShopOutputItem
from .player_building_shop_stock import PlayerBuildingShopStock
from ..common import BaseStruct


class PlayerBuildingShop(BaseStruct):
    stock: list[PlayerBuildingShopStock]
    outputItem: list[PlayerBuildingShopOutputItem]
