from pydantic import BaseModel, ConfigDict

from .player_recal_rune_season import PlayerRecalRuneSeason


class PlayerRecalRune(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    seasons: dict[str, PlayerRecalRuneSeason]
