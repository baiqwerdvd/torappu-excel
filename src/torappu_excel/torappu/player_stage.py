from .player_stage_state import PlayerStageState
from ..common import BaseStruct


class PlayerStage(BaseStruct):
    stageId: str
    completeTimes: int
    startTimes: int
    practiceTimes: int
    state: PlayerStageState
    hasBattleReplay: int
    noCostCnt: int | None = None
