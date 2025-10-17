from .player_recal_rune_reward import PlayerRecalRuneReward
from .player_recal_rune_stage import PlayerRecalRuneStage
from ..common import BaseStruct


class PlayerRecalRuneSeason(BaseStruct):
    stage: dict[str, PlayerRecalRuneStage]
    reward: PlayerRecalRuneReward
