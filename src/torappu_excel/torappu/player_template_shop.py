from .player_good_item_data import PlayerGoodItemData
from .player_good_progress_data import PlayerGoodProgressData
from ..common import BaseStruct


class PlayerTemplateShop(BaseStruct):
    coin: int
    info: list[PlayerGoodItemData]
    progressInfo: dict[str, PlayerGoodProgressData]
