from typing import Any

from msgspec import field

from .player_good_item_data import PlayerGoodItemData
from ..common import BaseStruct


class PlayerGiftProgressPerData(BaseStruct):
    info: list[PlayerGoodItemData]
    valid: list[Any] | None = field(default=None)
