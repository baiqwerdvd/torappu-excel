from .player_good_item_data import PlayerGoodItemData
from ..common import BaseStruct


class PlayerSocialShopData(BaseStruct):
    info: list[PlayerGoodItemData]
    charPurchase: dict[str, int]
    curShopId: str
