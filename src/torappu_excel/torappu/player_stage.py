from pydantic import BaseModel, ConfigDict

from .player_stage_state import PlayerStageState


class PlayerStage(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    completeTimes: int
    startTimes: int
    practiceTimes: int
    state: PlayerStageState
    hasBattleReplay: bool
    noCostCnt: int | None = None
