from pydantic import BaseModel, ConfigDict

from .player_six_star_tag_finish_state import PlayerSixStarTagFinishState


class PlayerSixStarStage(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    tagFinish: PlayerSixStarTagFinishState
    tagSelected: list[str]
