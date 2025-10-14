from pydantic import BaseModel, ConfigDict

from .player_stage_state import PlayerStageState


class PlayerActFun6Stage(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    achievements: dict[str, int]
    speedrunning: int
    state: PlayerStageState
