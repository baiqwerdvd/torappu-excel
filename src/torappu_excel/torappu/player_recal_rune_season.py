from pydantic import BaseModel, ConfigDict

from .player_recal_rune_reward import PlayerRecalRuneReward
from .player_recal_rune_stage import PlayerRecalRuneStage


class PlayerRecalRuneSeason(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stage: dict[str, PlayerRecalRuneStage]
    reward: PlayerRecalRuneReward
