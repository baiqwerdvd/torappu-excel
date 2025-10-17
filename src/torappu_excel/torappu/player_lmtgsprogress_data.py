from .player_good_item_data import PlayerGoodItemData
from ..common import BaseStruct


class PlayerLMTGSProgressData(BaseStruct):
    info: list[PlayerGoodItemData]
