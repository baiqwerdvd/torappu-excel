from pydantic import BaseModel, ConfigDict

from .player_gift_progress_per_data import PlayerGiftProgressPerData
from .player_gift_progress_rotate_data import PlayerGiftProgressRotateData


class PlayerGiftProgressData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    oneTime: PlayerGiftProgressPerData
    level: PlayerGiftProgressPerData
    weekly: PlayerGiftProgressRotateData
    monthly: PlayerGiftProgressRotateData
    choose: PlayerGiftProgressPerData | None = None
