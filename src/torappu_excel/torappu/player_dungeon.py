from .player_hidden_stage import PlayerHiddenStage
from .player_six_star import PlayerSixStar
from .player_special_stage import PlayerSpecialStage
from .player_stage import PlayerStage
from .player_zone import PlayerZone
from ..common import BaseStruct


class PlayerDungeon(BaseStruct):
    stages: dict[str, PlayerStage]
    cowLevel: dict[str, PlayerSpecialStage]
    hideStages: dict[str, PlayerHiddenStage]
    mainlineBannedStages: list[str]
    sixStar: PlayerSixStar
    zones: dict[str, PlayerZone] | None = None
