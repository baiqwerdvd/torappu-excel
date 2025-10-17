from .player_medal_custom_layout import PlayerMedalCustomLayout
from ..common import BaseStruct


class PlayerMedalCustom(BaseStruct):
    currentIndex: str
    customs: dict[str, PlayerMedalCustomLayout]
