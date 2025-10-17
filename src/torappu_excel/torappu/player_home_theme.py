from .player_home_unlock_status import PlayerHomeUnlockStatus
from ..common import BaseStruct


class PlayerHomeTheme(BaseStruct):
    selected: str
    themes: dict[str, PlayerHomeUnlockStatus]
