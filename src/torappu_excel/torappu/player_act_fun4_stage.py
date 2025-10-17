from .player_stage_state import PlayerStageState
from ..common import BaseStruct


class PlayerActFun4Stage(BaseStruct):
    state: PlayerStageState
    liveTimes: int
