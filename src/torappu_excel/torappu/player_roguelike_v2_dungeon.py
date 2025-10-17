from .player_roguelike_v2_zone import PlayerRoguelikeV2Zone
from ..common import BaseStruct


class PlayerRoguelikeV2Dungeon(BaseStruct):
    zones: dict[int, PlayerRoguelikeV2Zone]
    verticalCostDelta: int | None = None
