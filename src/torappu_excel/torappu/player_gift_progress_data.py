from .player_gift_progress_per_data import PlayerGiftProgressPerData
from .player_gift_progress_rotate_data import PlayerGiftProgressRotateData
from ..common import BaseStruct


class PlayerGiftProgressData(BaseStruct):
    oneTime: PlayerGiftProgressPerData
    level: PlayerGiftProgressPerData
    weekly: PlayerGiftProgressRotateData
    monthly: PlayerGiftProgressRotateData
    choose: PlayerGiftProgressPerData | None = None
