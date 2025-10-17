from .player_home_unlock_status import PlayerHomeUnlockStatus
from ..common import BaseStruct


class PlayerHomeBackground(BaseStruct):
    selected: str
    bgs: dict[str, PlayerHomeUnlockStatus]
