from pydantic import BaseModel, ConfigDict

from .player_six_star_milestone_item import PlayerSixStarMilestoneItem


class PlayerSixStarMilestone(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    point: int
    rewards: dict[str, PlayerSixStarMilestoneItem]
