from pydantic import BaseModel, ConfigDict

from .player_hidden_stage import PlayerHiddenStage
from .player_six_star import PlayerSixStar
from .player_special_stage import PlayerSpecialStage
from .player_stage import PlayerStage
from .player_zone import PlayerZone


class PlayerDungeon(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stages: dict[str, PlayerStage]
    zones: dict[str, PlayerZone] | None = None
    cowLevel: dict[str, PlayerSpecialStage]
    hideStages: dict[str, PlayerHiddenStage]
    mainlineBannedStages: list[str]
    sixStar: PlayerSixStar
