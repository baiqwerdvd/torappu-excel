from .player_medal_custom_layout_item import PlayerMedalCustomLayoutItem
from ..common import BaseStruct


class PlayerMedalCustomLayout(BaseStruct):
    layout: list[PlayerMedalCustomLayoutItem]
