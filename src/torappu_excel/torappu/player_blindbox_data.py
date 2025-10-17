from .player_good_item_data import PlayerGoodItemData
from ..common import BaseStruct


class PlayerBlindboxData(BaseStruct):
    info: list[PlayerGoodItemData]
