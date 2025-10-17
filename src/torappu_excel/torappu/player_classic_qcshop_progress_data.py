from .player_good_item_data import PlayerGoodItemData
from .player_good_progress_data import PlayerGoodProgressData
from ..common import BaseStruct


class PlayerClassicQCShopProgressData(BaseStruct):
    info: list[PlayerGoodItemData]
    progressInfo: dict[str, PlayerGoodProgressData]
