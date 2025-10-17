from .player_good_item_data import PlayerGoodItemData
from ..common import BaseStruct


class PlayerGiftProgressRotateData(BaseStruct):
    curGroupId: str
    info: list[PlayerGoodItemData]
