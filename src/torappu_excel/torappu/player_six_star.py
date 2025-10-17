from .player_six_star_milestone import PlayerSixStarMilestone
from .player_six_star_stage import PlayerSixStarStage
from ..common import BaseStruct


class PlayerSixStar(BaseStruct):
    stages: dict[str, PlayerSixStarStage]
    groups: dict[str, PlayerSixStarMilestone]
