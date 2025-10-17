from .player_home_condition_progress import PlayerHomeConditionProgress
from ..common import BaseStruct


class PlayerHomeUnlockStatus(BaseStruct):
    unlock: int | None = None
    conditions: dict[str, PlayerHomeConditionProgress] | None = None
