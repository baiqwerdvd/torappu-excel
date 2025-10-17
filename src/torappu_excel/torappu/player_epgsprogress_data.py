from .player_good_item_data import PlayerGoodItemData
from ..common import BaseStruct


class PlayerEPGSProgressData(BaseStruct):
    info: list[PlayerGoodItemData]
