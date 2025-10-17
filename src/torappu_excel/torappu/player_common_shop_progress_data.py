from .player_good_item_data import PlayerGoodItemData
from ..common import BaseStruct


class PlayerCommonShopProgressData(BaseStruct):
    curShopId: str
    info: list[PlayerGoodItemData]
    lastClick: int
