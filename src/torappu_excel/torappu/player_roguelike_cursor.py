from .player_roguelike_state import PlayerRoguelikeState
from .roguelike_node_position import RoguelikeNodePosition
from ..common import BaseStruct


class PlayerRoguelikeCursor(BaseStruct):
    zoneIndex: int
    position: RoguelikeNodePosition
    state: PlayerRoguelikeState
