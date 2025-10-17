from .player_recal_rune_season import PlayerRecalRuneSeason
from ..common import BaseStruct


class PlayerRecalRune(BaseStruct):
    seasons: dict[str, PlayerRecalRuneSeason]
