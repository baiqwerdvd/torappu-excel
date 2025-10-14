from pydantic import BaseModel, ConfigDict

from .player_stage_state import PlayerStageState


class PlayerActFunStage(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    state: PlayerStageState
    scores: list[int]
