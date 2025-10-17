from .player_good_item_data import PlayerGoodItemData
from ..common import BaseStruct


class PlayerFurnitureShopData(BaseStruct):
    info: list[PlayerGoodItemData]
    groupInfo: dict[str, int]
