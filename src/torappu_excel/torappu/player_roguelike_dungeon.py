from .player_roguelike_zone import PlayerRoguelikeZone
from ..common import BaseStruct


class PlayerRoguelikeDungeon(BaseStruct):
    zones: dict[int, PlayerRoguelikeZone]
