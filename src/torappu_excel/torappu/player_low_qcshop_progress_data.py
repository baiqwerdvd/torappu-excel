from msgspec import field

from .player_good_item_data import PlayerGoodItemData
from ..common import BaseStruct


class PlayerLowQCShopProgressData(BaseStruct):
    curGroupId: str
    curShopId: str
    info: list[PlayerGoodItemData]
    lggCostTotal: int | None = field(default=None)
