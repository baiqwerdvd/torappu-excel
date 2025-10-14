from pydantic import BaseModel, ConfigDict

from .player_stage_state import PlayerStageState


class PlayerActFun4Stage(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    state: PlayerStageState
    liveTimes: int
