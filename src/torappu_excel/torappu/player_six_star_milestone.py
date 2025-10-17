from .player_six_star_milestone_item import PlayerSixStarMilestoneItem
from ..common import BaseStruct


class PlayerSixStarMilestone(BaseStruct):
    point: int
    rewards: dict[str, PlayerSixStarMilestoneItem]
