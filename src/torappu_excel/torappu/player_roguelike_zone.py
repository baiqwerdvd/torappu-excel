from .player_roguelike_node import PlayerRoguelikeNode
from ..common import BaseStruct


class PlayerRoguelikeZone(BaseStruct):
    zoneId: str
    nodes: dict[int, PlayerRoguelikeNode]
