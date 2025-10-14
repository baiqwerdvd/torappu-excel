from pydantic import BaseModel, ConfigDict

from .player_home_unlock_status import PlayerHomeUnlockStatus


class PlayerHomeTheme(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    selected: str
    themes: dict[str, PlayerHomeUnlockStatus]
