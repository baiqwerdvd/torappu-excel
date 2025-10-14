from pydantic import BaseModel, ConfigDict

from .player_six_star_milestone import PlayerSixStarMilestone
from .player_six_star_stage import PlayerSixStarStage


class PlayerSixStar(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stages: dict[str, PlayerSixStarStage]
    groups: dict[str, PlayerSixStarMilestone]
