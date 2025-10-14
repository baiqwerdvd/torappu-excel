from pydantic import BaseModel, ConfigDict

from .player_medal_custom import PlayerMedalCustom
from .player_per_medal import PlayerPerMedal


class PlayerMedal(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    medals: dict[str, PlayerPerMedal]
    custom: PlayerMedalCustom
