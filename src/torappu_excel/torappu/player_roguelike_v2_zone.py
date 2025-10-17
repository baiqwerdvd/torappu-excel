from .player_roguelike_node import PlayerRoguelikeNode
from .player_roguelike_zone_type import PlayerRoguelikeZoneType
from ..common import BaseStruct


class PlayerRoguelikeV2Zone(BaseStruct):
    id: str
    nodes: dict[int, PlayerRoguelikeNode]
    variation: list[str]
    type: PlayerRoguelikeZoneType
