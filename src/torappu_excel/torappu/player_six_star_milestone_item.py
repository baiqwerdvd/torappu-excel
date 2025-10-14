from pydantic import BaseModel, ConfigDict

from .player_six_star_milestone_state import PlayerSixStarMilestoneState


class PlayerSixStarMilestoneItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    state: PlayerSixStarMilestoneState
