from .player_stage_state import PlayerStageState
from ..common import BaseStruct


class PlayerActFun6Stage(BaseStruct):
    stageId: str
    achievements: dict[str, int]
    speedrunning: int
    state: PlayerStageState
