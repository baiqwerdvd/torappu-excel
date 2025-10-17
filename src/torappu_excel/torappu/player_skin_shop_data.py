from .player_blindbox_data import PlayerBlindboxData
from .player_good_item_data import PlayerGoodItemData
from ..common import BaseStruct


class PlayerSkinShopData(BaseStruct):
    gachaGood: PlayerBlindboxData
    info: list[PlayerGoodItemData] | None = None
